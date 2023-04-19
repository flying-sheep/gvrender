from __future__ import annotations

from collections.abc import Generator, MutableMapping
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

class AGraph:
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

class Attribute(MutableMapping):
    def __getitem__(self, name: str) -> str: ...
    def __setitem__(self, name: str, value: str) -> None: ...
    def __delitem__(self, name: str) -> None: ...
    def __iter__(self) -> Generator[str, None, None]: ...
    def __len__(self) -> int: ...
