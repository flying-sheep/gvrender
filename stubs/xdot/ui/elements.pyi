from typing import Literal, Optional

from xdot.ui.pen import Pen

class Shape:
    bounding: tuple[float, float, float, float]
    def get_text(self) -> Optional[str]: ...

class TextShape(Shape):
    pen: Pen
    x: float
    y: float
    j: int
    """Centering"""
    w: float
    """Width"""
    t: str
    """Text"""

class ImageShape(Shape): ...  # TODO

class EllipseShape(Shape):
    pen: Pen
    x0: float
    y0: float
    w: float
    h: float
    filled: bool

class PolygonShape(Shape): ...  # TODO

class LineShape(Shape):
    pen: Pen
    points: list[tuple[float, float]]

class BezierShape(Shape):
    pen: Pen
    points: list[tuple[float, float]]
    filled: bool

class CompoundShape(Shape):
    shapes: list[Shape]

class Element(CompoundShape): ...  # TODO

class Node(Element):
    id: str
    x: float
    y: float
    x1: float
    y1: float
    x2: float
    y2: float
    url: str

class Edge(Element):
    src: Node
    dst: Node
    points: list[tuple[float, float]]

class Graph(Shape):
    width: int
    height: int
    shapes: list[Shape]
    nodes: list[Node]
    edges: list[Edge]
    outputorder: Literal['breadthfirst', 'edgesfirst']
