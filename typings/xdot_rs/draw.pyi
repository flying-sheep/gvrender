from enum import Enum
from typing import ClassVar

class Rgba:
    r: int
    g: int
    b: int
    a: int

class FontCharacteristics(int):
    BOLD: ClassVar[int]
    ITALIC: ClassVar[int]
    UNDERLINE: ClassVar[int]
    SUPERSCRIPT: ClassVar[int]
    SUBSCRIPT: ClassVar[int]
    STRIKE_THROUGH: ClassVar[int]
    OVERLINE: ClassVar[int]

class Style(Enum):
    Dashed = ...
    Dotted = ...
    Solid = ...
    Invis = ...
    Bold = ...

class Pen:
    color: Rgba
    fill_color: Rgba
    line_width: float
    line_style: Style
    font_size: float
    font_name: str
    font_characteristics: FontCharacteristics
