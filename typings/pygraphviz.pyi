from __future__ import annotations

from collections.abc import Collection, Generator, MutableMapping
from pathlib import Path
from typing import Literal

class SWIGPointer: ...

_Format = Literal[
    'canon',
    'cmap',
    'cmapx',
    'cmapx_np',
    'dia',
    'dot',
    'fig',
    'gd',
    'gd2',
    'gif',
    'hpgl',
    'imap',
    'imap_np',
    'ismap',
    'jpe',
    'jpeg',
    'jpg',
    'mif',
    'mp',
    'pcl',
    'pdf',
    'pic',
    'plain',
    'plain-ext',
    'png',
    'ps',
    'ps2',
    'svg',
    'svgz',
    'vml',
    'vmlz',
    'vrml',
    'vtx',
    'wbmp',
    'xdot',
    'xlib',
]

class Node(str):
    attr: ItemAttribute
    name: str

class Edge(tuple[Node, Node]):
    attr: ItemAttribute
    name: str
    key: str

class AGraph(Collection[Node]):
    handle: SWIGPointer
    graph_attr: Attribute
    node_attr: Attribute
    edge_attr: Attribute
    def __init__(
        self,
        thing: str | Path | dict | SWIGPointer = None,
        filename: str | Path = None,
        data: dict = None,
        string: str = None,
        handle: SWIGPointer = None,
        name: str = '',
        strict: bool = True,
        directed: bool = False,
        **attr,
    ) -> None: ...
    def draw(
        self,
        path: str | None = None,
        format: _Format | None = None,
        prog: Literal['neato', 'dot', 'twopi', 'circo', 'fdp', 'nop'] | None = None,
        args: str = '',
    ): ...
    def nodes_iter(self) -> Generator[Node, None, None]: ...
    def edges_iter(self) -> Generator[Edge, None, None]: ...
    def neighbors_iter(self, n: Node | str) -> Generator[Node, None, None]: ...
    def __getitem__(self, n: Node | str) -> list[Node]: ...

class Attribute(MutableMapping[str]):
    pass

class ItemAttribute(Attribute):
    pass
