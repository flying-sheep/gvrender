from __future__ import annotations

from collections.abc import Collection, Mapping
from typing import Any, Literal

from matplotlib.artist import Artist
from matplotlib.path import Path
from matplotlib.transform import Transform

from ._types import _Color

class Patch(Artist):
    def __init__(
        self,
        edgecolor: _Color | Literal['auto'] | None = None,
        facecolor: _Color | None = None,
        color: _Color | None = None,
        linewidth: float | None = None,
        linestyle: (
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
            ]
            | tuple[int, Collection[int]]
            | None
        ) = None,
        antialiased: bool | None = None,
        hatch: Literal['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'] | None = None,
        fill: bool = True,
        capstyle=None,
        joinstyle=None,
        **kwargs,
    ) -> None: ...
    # TODO: more
    transform: Transform
    # TODO: more

class Shadow(Patch):
    def __init__(
        self, patch: Patch, ox: float, oy: float, props: Mapping[str, Any] = None, **kwargs
    ) -> None: ...

class Rectangle(Patch):
    def __init__(
        self, xy: tuple[float, float], width: float, height: float, angle: float = 0.0, **kwargs
    ) -> None: ...

class RegularPolygon(Patch): ...

class PathPatch(Patch):
    def __init__(self, path: Path, **kwargs) -> None: ...

class StepPatch(PathPatch): ...
class Polygon(Patch): ...
class Wedge(Patch): ...
class Arrow(Patch): ...
class FancyArrow(Polygon): ...
class CirclePolygon(RegularPolygon): ...

class Ellipse(Patch):
    def __init__(
        self, xy: tuple[float, float], width: float, height: float, angle: float = 0, **kwargs
    ) -> None: ...

class Circle(Ellipse): ...
class Arc(Ellipse): ...

# TODO: styles

class FancyBboxPatch(Patch): ...
class FancyArrowPatch(Patch): ...
class ConnectionPatch(FancyArrowPatch): ...
