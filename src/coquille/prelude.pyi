import abc
import collections.abc
import typing

from coquille.sequences import EscapeSequence, EscapeSequenceName
from coquille.typeshed import SupportsWriteAndFlush

P = typing.ParamSpec("P")

@typing.overload
def prepare(
    sequence: EscapeSequence | EscapeSequenceName,
) -> EscapeSequence:  # pragma: no cover
    pass

@typing.overload
def prepare(
    sequence: collections.abc.Callable[P, EscapeSequence],
    *args: P.args,
    **kwargs: P.kwargs,
) -> EscapeSequence:  # pragma: no cover
    pass

@typing.overload
def apply(
    sequence: EscapeSequence | EscapeSequenceName,
    file: SupportsWriteAndFlush[str] | None = None,
) -> None:  # pragma: no cover
    pass

@typing.overload
def apply(
    sequence: collections.abc.Callable[P, EscapeSequence],
    file: SupportsWriteAndFlush[str] | None = None,
    *args: P.args,
    **kwargs: P.kwargs,
) -> None:  # pragma: no cover
    pass

class CoquilleLike(typing.Protocol):
    sequences: list[EscapeSequence]
    file: SupportsWriteAndFlush[str] | None

    @abc.abstractmethod
    def print(
        self,
        *values: object,
        sep: str | None = None,
        end: str | None = "\n",
    ) -> None:
        pass

class _ContextCoquille:
    sequences: list[EscapeSequence]
    file: SupportsWriteAndFlush[str] | None

    def apply(self, sequence: EscapeSequence | EscapeSequenceName) -> None: ...
    def reset(self) -> None: ...
    def print(
        self,
        *values: object,
        sep: str | None = None,
        end: str | None = "\n",
    ) -> None: ...

class Coquille:
    sequences: list[EscapeSequence]
    file: SupportsWriteAndFlush[str] | None

    @typing.overload
    @classmethod
    def new(
        cls: type[typing.Self],
        *sequences: EscapeSequence | EscapeSequenceName,
    ) -> typing.Self:  # pragma: no cover
        ...
    @typing.overload
    @classmethod
    def new(
        cls: type[typing.Self],
        *sequences: EscapeSequence | EscapeSequenceName,
        file: SupportsWriteAndFlush[str],
    ) -> typing.Self:  # pragma: no cover
        ...
    def print(
        self: CoquilleLike,
        *values: object,
        sep: str | None = " ",
        end: str | None = "\n",
    ) -> None: ...
    def write(
        self,
        text: str,
        end: str | None = "\n",
    ) -> None: ...
    def __enter__(self) -> _ContextCoquille: ...
    def __exit__(self, *_) -> None: ...

def write(
    text: str,
    *sequences: EscapeSequence | EscapeSequenceName,
    end: str | None = "\n",
    file: SupportsWriteAndFlush[str] | None = None,
) -> None: ...
