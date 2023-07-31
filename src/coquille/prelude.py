# pyright: reportUnusedCallResult = false
from __future__ import annotations

import sys
from abc import abstractmethod
from collections.abc import Callable
from dataclasses import dataclass
from typing import overload
from typing import Protocol
from typing import TYPE_CHECKING

from coquille.sequences import EscapeSequence
from coquille.sequences import EscapeSequenceName
from coquille.sequences import get_sequence_from_name
from coquille.sequences import soft_reset

__all__ = [
    "apply",
    "Coquille",
    "EscapeSequence",
    "EscapeSequenceName",
    "prepare",
    "write",
]


# ... don't say anything.
if TYPE_CHECKING:  # pragma: no cover
    if sys.version_info >= (3, 10):
        from typing import ParamSpec

        P = ParamSpec("P")

    from coquille.typeshed import Self
    from coquille.typeshed import SupportsWrite


@overload
def prepare(
    sequence: EscapeSequence | EscapeSequenceName,
) -> EscapeSequence:  # pragma: no cover
    pass


@overload
def prepare(
    sequence: Callable[P, EscapeSequence],
    *args: P.args,
    **kwargs: P.kwargs,
) -> EscapeSequence:  # pragma: no cover
    pass


def prepare(
    sequence: EscapeSequence | EscapeSequenceName | Callable[P, EscapeSequence],
    *args: P.args,
    **kwargs: P.kwargs,
) -> EscapeSequence:
    """
    Prepare an escape sequence.

    If `sequence` is already one, it is returned ; else, it passes
    the arguments to the escape sequence factory to construct one.
    """

    if isinstance(sequence, EscapeSequence):
        return sequence
    elif isinstance(sequence, str):
        return get_sequence_from_name(sequence)

    return sequence(*args, **kwargs)


@overload
def apply(
    sequence: EscapeSequence | EscapeSequenceName,
    file: SupportsWrite[str] | None = None,
) -> None:  # pragma: no cover
    pass


@overload
def apply(
    sequence: Callable[P, EscapeSequence],
    file: SupportsWrite[str] | None = None,
    *args: P.args,
    **kwargs: P.kwargs,
) -> None:  # pragma: no cover
    pass


def apply(
    sequence: EscapeSequence | EscapeSequenceName | Callable[P, EscapeSequence],
    file: SupportsWrite[str] | None = None,
    *args: P.args,
    **kwargs: P.kwargs,
) -> None:
    """
    Apply an escape sequence to a stream (by default, stdout).
    """

    string: EscapeSequence = prepare(sequence, *args, **kwargs)
    target = file or sys.stdout
    target.write(string)


class CoquilleLike(Protocol):
    sequences: list[EscapeSequence]
    file: SupportsWrite[str] | None

    @abstractmethod
    def print(
        self,
        *values: object,
        sep: str | None = None,
        end: str | None = "\n",
    ) -> None:
        pass


@dataclass(slots=True)
class _ContextCoquille:
    sequences: list[EscapeSequence]
    file: SupportsWrite[str] | None

    def apply(self, sequence: EscapeSequence | EscapeSequenceName) -> None:
        """
        Apply an escape sequence in the context manager of a Coquille
        in live.

        It is not added to the base `coquille.sequences`, but will still
        be reset at the end of the block.
        """

        apply(sequence, self.file)

    def reset(self) -> None:
        """
        Reset the currently active escape sequences of the `with` block.
        """

        apply(soft_reset, self.file)

    def print(
        self,
        *values: object,
        sep: str | None = None,
        end: str | None = "\n",
    ) -> None:
        """
        Convenient function to print in the same file as the coquille's one.

        ## Example

        ```py
        >>> with Coquille.new(bold, fg_red, file=sys.stderr) as coquille:
        ...     # same as: print("My pretty error message", file=coquille.file)
        ...     coquille.print("My pretty error message")
        ```
        """

        Coquille.print(self, *values, sep=sep, end=end)


@dataclass(slots=True)
class Coquille:
    sequences: list[EscapeSequence]
    file: SupportsWrite[str] | None

    @overload
    @classmethod
    def new(
        cls: type[Self],
        *sequences: EscapeSequence | EscapeSequenceName,
    ) -> Self:  # pragma: no cover
        pass

    @overload
    @classmethod
    def new(
        cls: type[Self],
        *sequences: EscapeSequence | EscapeSequenceName,
        file: SupportsWrite[str],
    ) -> Self:  # pragma: no cover
        pass

    @classmethod
    def new(
        cls: type[Self],
        *sequences: EscapeSequence | EscapeSequenceName,
        file: SupportsWrite[str] | None = None,
    ) -> Self:
        """
        Convenient constructor for a Coquille.
        """

        return cls(list(sequences), file)

    def print(
        self: CoquilleLike,
        *values: object,
        sep: str | None = " ",
        end: str | None = "\n",
    ) -> None:
        """
        Convenient function to print in the same file as the coquille's one.

        ## Example

        ```py
        >>> my_coquille = Coquille.new(bold, fg_red, file=sys.stderr)
        >>> # same as: print("My pretty error message", file=my_coquille.file)
        >>> my_coquille.print("My pretty error message")
        ```
        """

        for sequence in self.sequences:
            apply(sequence, self.file)

        print(*values, sep=sep, end=end, file=self.file)
        apply(soft_reset)

    def write(
        self,
        text: str,
        end: str | None = "\n",
    ) -> None:
        """
        A function relatively similar to built-in `print`.
        It is the same as naked `write`, but it uses the coquille's
        registered sequences.

        Example:
        ```py
        >>> from coquille import Coquille
        >>> from coquille.sequences import fg_magenta, italic
        >>> my_coquille = Coquille.new(fg_magenta, italic)
        >>> my_coquille.write("Hello World!")
        Hello World!
        ```
        Here, "Hello World!" is printed in italic and magenta, but this
        cannot be reproduced exactly in docstrings.

        The previous example is roughly equivalent to:
        ```py
        >>> print("\x1b[35m", end="")
        >>> print("\x1b[3m", end="")
        >>> print("Hello World!")
        >>> print("\x1b[!p", end="")
        ```

        Note that the soft reset sequence is used rather than SGR reset `x1b[0m`,
        because the range of allowed escape sequences is larger than SGR.
        """

        self.print(text, end=end)

    def __enter__(self) -> _ContextCoquille:
        """
        Set up a context for a Coquille.

        The returned object is actually of a different type ;
        this is for convenience, allowing to have methods that
        only make sense inside the `with` block, such as `coquille.reset()`.
        """

        for sequence in self.sequences:
            apply(sequence, self.file)

        return _ContextCoquille(self.sequences, self.file)

    def __exit__(self, *_) -> None:
        """
        Leave the Coquille context.

        Soft reset the escape sequences applied since then.
        """

        apply(soft_reset, self.file)


def write(
    text: str,
    *sequences: EscapeSequence | EscapeSequenceName,
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
) -> None:
    """
    A function relatively similar to built-in `print`, but with
    support of escape sequences that are prepended to the printed
    text.

    Example:
    ```py
    >>> from coquille.sequences import fg_magenta, italic
    >>> Coquille.write("Hello World!", fg_magenta, italic)
    Hello World!
    ```
    Here, "Hello World!" is printed in italic and magenta, but this
    cannot be reproduced exactly in docstrings.

    The previous example is roughly the same as doing:
    ```py
    >>> print("\x1b[35m", end="")
    >>> print("\x1b[3m", end="")
    >>> print("Hello World!")
    >>> print("\x1b[!p", end="")
    ```

    Note that the soft reset sequence is used rather than SGR reset `x1b[0m`,
    because the range of allowed escape sequences is larger than SGR.
    """

    for sequence in sequences:
        apply(sequence, file)

    print(text, end=end, file=file)
    apply(soft_reset)
