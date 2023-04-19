from collections.abc import Sequence
from enum import Enum


class Ellipse:
    filled: bool
    x: float
    y: float
    w: float
    h: float

class PointsType(Enum):
    Polygon = ...
    Polyline = ...
    BSpline = ...

class Points(Shape):
    filled: bool
    type: PointsType
    points: Sequence[tuple[float, float]]

class TextAlign(Enum):
    Left = ...
    Center = ...
    Right = ...

class Text:
    x: float
    y: float
    align: TextAlign
    width: float
    text: str

class ExternalImage:
    pass

Shape = Ellipse | Points | Text | ExternalImage
