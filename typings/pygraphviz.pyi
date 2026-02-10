from __future__ import annotations

from collections.abc import Collection, Generator, Iterable, Iterator, Mapping, MutableMapping
from pathlib import Path
from typing import Literal, overload

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

_Prog = Literal['neato', 'dot', 'twopi', 'circo', 'fdp', 'nop']

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
        thing: str | Path | Mapping[str, Iterable[str]] | SWIGPointer | None = None,
        filename: str | Path | None = None,
        data: Mapping[str, Iterable[str]] | None = None,
        string: str | None = None,
        handle: SWIGPointer | None = None,
        name: str = '',
        strict: bool = True,
        directed: bool = False,
        **attr: object,
    ) -> None: ...
    @overload
    def draw(
        self,
        path: None = None,
        format: _Format | None = None,
        prog: _Prog | None = None,
        args: str = '',
    ) -> bytes: ...
    @overload
    def draw(
        self,
        path: str,
        format: _Format | None = None,
        prog: _Prog | None = None,
        args: str = '',
    ) -> None: ...
    def nodes_iter(self) -> Generator[Node]: ...
    def edges_iter(self) -> Generator[Edge]: ...
    def neighbors_iter(self, n: Node | str) -> Generator[Node]: ...
    def __getitem__(self, n: Node | str) -> list[Node]: ...
    def __contains__(self, n: Node | str) -> bool: ...  # type: ignore[override]
    def __iter__(self) -> Generator[Node]: ...
    def __len__(self) -> int: ...

class Attribute(MutableMapping[str, str]):
    def __delitem__(self, __key: str) -> None: ...
    def __getitem__(self, __key: str) -> str: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __setitem__(self, __key: str, __value: str) -> None: ...

class ItemAttribute(Attribute):
    pass
