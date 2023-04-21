from __future__ import annotations

from . import draw, shapes

__all__ = ['draw', 'shapes', 'ShapeDraw', 'parse']

class ShapeDraw:
    pen: draw.Pen
    shape: shapes.Shape

def parse(code: str) -> list[ShapeDraw]: ...
