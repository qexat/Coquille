"""
Typeshed stuff that Coquille needs but that are not available
on the Python standard library.
"""
from abc import abstractmethod
from typing import Protocol
from typing import TypeVar

_T_contra = TypeVar("_T_contra", contravariant=True)

class SupportsWriteAndFlush(Protocol[_T_contra]):
    @abstractmethod
    def write(self, __s: _T_contra) -> object:
        pass

    @abstractmethod
    def flush(self) -> None:
        pass

Self = TypeVar("Self")
