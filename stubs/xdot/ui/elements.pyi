from typing import Literal

from xdot.ui.pen import Pen

class Shape:
    bounding: tuple[float, float, float, float]

class TextShape(Shape): ...
class ImageShape(Shape): ...
class EllipseShape(Shape): ...
class PolygonShape(Shape): ...

class LineShape(Shape):
    pen: Pen
    points: list[tuple[float, float]]

class BezierShape(Shape):
    pen: Pen
    points: list[tuple[float, float]]
    filled: bool

class CompoundShape(Shape):
    shapes: list[Shape]

class Element(CompoundShape): ...

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
