"""
Typeshed stuff that Coquille needs but that are not available
on the Python standard library.
"""

from typing import Protocol, TypeVar


_T_contra = TypeVar("_T_contra", contravariant=True)


class SupportsWrite(Protocol[_T_contra]):
    def write(self, __s: _T_contra) -> object:
        ...


class SupportsWriteAndFlush(SupportsWrite[_T_contra], Protocol[_T_contra]):
    def flush(self) -> None:
        ...
