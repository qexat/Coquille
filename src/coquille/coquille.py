from __future__ import annotations

import sys
from collections.abc import Callable
from dataclasses import dataclass
from typing import overload
from typing import TYPE_CHECKING

from coquille.sequences import EscapeSequence
from coquille.sequences import soft_reset

__all__ = ["apply", "Coquille", "EscapeSequence", "prepare"]

# ... don't say anything.
if TYPE_CHECKING:  # pragma: no cover
    if sys.version_info >= (3, 10):
        from typing import ParamSpec

        P = ParamSpec("P")

    from coquille.typeshed import Self
    from coquille.typeshed import SupportsWrite


@overload
def prepare(sequence: EscapeSequence) -> EscapeSequence:  # pragma: no cover
    pass


@overload
def prepare(
    sequence: Callable[P, EscapeSequence],
    *args: P.args,
    **kwargs: P.kwargs,
) -> EscapeSequence:  # pragma: no cover
    pass


def prepare(
    sequence: EscapeSequence | Callable[P, EscapeSequence],
    *args: P.args,
    **kwargs: P.kwargs,
) -> EscapeSequence:
    """
    Prepare an escape sequence.

    If `sequence` is already one, it is returned ; else, it passes
    the arguments to the escape sequence factory to construct one.
    """

    if isinstance(sequence, str):
        return sequence

    return sequence(*args, **kwargs)


@overload
def apply(
    sequence: EscapeSequence,
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
    sequence: EscapeSequence | Callable[P, EscapeSequence],
    file: SupportsWrite[str] | None = None,
    *args: P.args,
    **kwargs: P.kwargs,
) -> None:
    """
    Apply an escape sequence to a stream (by default, stdout).
    """

    string: EscapeSequence = prepare(sequence, *args, **kwargs)
    target = file or sys.stdout
    target.write(string)  # type: ignore[unused]


class _ContextCoquille:
    __slots__ = ("__sequences", "__file")  # private slots

    def __init__(
        self,
        sequences: list[EscapeSequence],
        file: SupportsWrite[str] | None,
    ) -> None:
        self.__sequences = sequences
        self.__file = file

    @property
    def sequences(self) -> list[EscapeSequence]:
        """
        Read-only ; the base sequences that were applied at the
        beginning of the `with` block. They are reset when the
        block ends.
        """

        return self.__sequences

    @property
    def file(self) -> SupportsWrite[str] | None:
        """
        Read-only ; the file where the sequences are printed in.
        """

        return self.__file

    def apply(self, sequence: EscapeSequence) -> None:
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


@dataclass(slots=True)
class Coquille:
    sequences: list[EscapeSequence]
    file: SupportsWrite[str] | None

    @overload
    @classmethod
    def new(cls: type[Self], *sequences: EscapeSequence) -> Self:  # pragma: no cover
        pass

    @overload
    @classmethod
    def new(
        cls: type[Self],
        *sequences: EscapeSequence,
        file: SupportsWrite[str],
    ) -> Self:  # pragma: no cover
        pass

    @classmethod
    def new(
        cls: type[Self],
        *sequences: EscapeSequence,
        file: SupportsWrite[str] | None = None,
    ) -> Self:
        """
        Convenient constructor for a Coquille.
        """

        return cls(list(sequences), file)

    @staticmethod
    def print(
        text: str,
        *sequences: EscapeSequence,
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
        >>> Coquille.print("Hello World!", fg_magenta, italic)
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

    def __enter__(self):
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
