"""
Typeshed stuff that Coquille needs but that are not available
on the Python standard library.
"""
from typing import Protocol
from typing import TypeVar


_T_contra = TypeVar("_T_contra", contravariant=True)


class SupportsWrite(Protocol[_T_contra]):
    def write(self, __s: _T_contra) -> object:
        ...


Self = TypeVar("Self")
