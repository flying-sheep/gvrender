from __future__ import annotations

from collections.abc import Collection, Sequence
from typing import ClassVar

from numpy import ndarray, uint8
from numpy.ma import MaskedArray

class Path:
    code_type: ClassVar[type[uint8]]
    STOP: ClassVar[uint8]  # 1 vertex
    MOVETO: ClassVar[uint8]  # 1 vertex
    LINETO: ClassVar[uint8]  # 1 vertex
    CURVE3: ClassVar[uint8]  # 2 vertices
    CURVE4: ClassVar[uint8]  # 3 vertices
    CLOSEPOLY: ClassVar[uint8]  # 1 vertex
    NUM_VERTICES_FOR_CODE: ClassVar[dict[uint8, int]]
    def __init__(
        self,
        vertices: Sequence[tuple[float, float]] | ndarray | MaskedArray,
        codes: Collection[uint8] = None,
        _interpolation_steps: int = 1,
        closed: bool = False,
        readonly: bool = False,
    ) -> None: ...
