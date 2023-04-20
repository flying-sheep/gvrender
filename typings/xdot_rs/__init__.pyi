from __future__ import annotations

from .draw import Pen
from .shapes import Shape

class ShapeDraw:
    pen: Pen
    shape: Shape

def parse(code: str) -> list[ShapeDraw]: ...
