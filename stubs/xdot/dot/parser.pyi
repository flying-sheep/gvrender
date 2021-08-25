from typing import Any, ClassVar

from ..ui.elements import Edge, Graph, Node, Shape

class Parser:
    lexer: Any
    lookahead: Any

class DotParser:
    graph_attrs: dict[str, bytes]
    node_attrs: dict[str, bytes]
    edge_attrs: dict[str, bytes]

class XDotParser(DotParser):
    XDOTVERSION: ClassVar[str]

    nodes: list[Node]
    edges: list[Edge]
    shapes: list[Shape]
    node_by_name: dict[str, Node]
    top_graph: bool
    width: int
    height: int
    outputorder = 'breadthfirst'
    def __init__(self, xdotcode: bytes) -> None: ...
    def parse(self) -> Graph: ...
