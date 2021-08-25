import collections.abc as cabc
from typing import Any, Literal, Optional, Union

from matplotlib.artist import Artist
from matplotlib.path import Path

_Color = Any

class Patch(Artist):
    def __init__(
        self,
        edgecolor: Union[_Color, Literal['auto'], None] = None,
        facecolor: Optional[_Color] = None,
        color: Optional[_Color] = None,
        linewidth: Optional[float] = None,
        linestyle: Union[
            Literal[
                '-',
                'solid',
                '--',
                'dashed',
                '-.',
                'dashdot',
                ':',
                'dotted',
                'None',
                'none',
                ' ',
                '',
            ],
            tuple[int, cabc.Collection[int]],
            None,
        ] = None,
        antialiased: Optional[bool] = None,
        hatch: Optional[Literal['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']] = None,
        fill: bool = True,
        capstyle=None,
        joinstyle=None,
        **kwargs
    ) -> None: ...

class Shadow(Patch):
    def __init__(
        self, patch: Patch, ox: float, oy: float, props: cabc.Mapping[str, Any] = None, **kwargs
    ) -> None: ...

class Rectangle(Patch):
    def __init__(
        self, xy: tuple[float, float], width: float, height: float, angle: float = 0.0, **kwargs
    ) -> None: ...

class PathPatch(Patch):
    def __init__(self, path: Path, **kwargs) -> None: ...
