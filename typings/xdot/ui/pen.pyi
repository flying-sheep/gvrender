import collections.abc as cabc
from typing import ClassVar

class Pen:
    BOLD: ClassVar[int]
    ITALIC: ClassVar[int]
    UNDERLINE: ClassVar[int]
    SUPERSCRIPT: ClassVar[int]
    SUBSCRIPT: ClassVar[int]
    STRIKE_THROUGH: ClassVar[int]
    OVERLINE: ClassVar[int]
    color: tuple[float, float, float, float]
    fillcolor: tuple[float, float, float, float]
    linewidth: float
    fontsize: float
    fontname: str
    bold: bool
    italic: bool
    underline: bool
    superscript: bool
    subscript: bool
    strikethrough: bool
    overline: bool
    dash: cabc.Sequence[float]
    def copy(self) -> Pen: ...
    def highlighted(self) -> Pen: ...
