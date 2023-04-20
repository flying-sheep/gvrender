from __future__ import annotations

from enum import Enum

class Rgba:
    r: int
    g: int
    b: int
    a: int

class FontCharacteristics:
    bits: int
    bold: bool
    italic: bool
    underline: bool
    superscript: bool
    subscript: bool
    strike_through: bool
    overline: bool

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
