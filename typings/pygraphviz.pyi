import collections.abc as cabc
from pathlib import Path
from typing import Literal, Optional, Union

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
        thing: Union[str, Path, dict, SWIGPointer] = None,
        filename: Union[str, Path] = None,
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
        path: Optional[str] = None,
        format: Optional[_Format] = None,
        prog: Optional[Literal['neato', 'dot', 'twopi', 'circo', 'fdp', 'nop']] = None,
        args: str = '',
    ): ...

class Attribute(cabc.MutableMapping):
    def __getitem__(self, name: str) -> str: ...
    def __setitem__(self, name: str, value: str) -> None: ...
    def __delitem__(self, name: str) -> None: ...
    def __iter__(self) -> cabc.Generator[str, None, None]: ...
    def __len__(self) -> int: ...
