from __future__ import annotations

import sys
from collections.abc import Collection, Mapping
from typing import Any, Literal, TypedDict

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

from matplotlib.artist import Artist
from matplotlib.path import Path
from matplotlib.transform import Transform
from numpy.typing import ArrayLike

from ._enums import CapStyle, JoinStyle
from ._types import _Color

# TODO: inherit from ArtistArgs
class PatchArgs(TypedDict, total=False):
    edgecolor: _Color | Literal['auto'] | None
    facecolor: _Color | None
    color: _Color | None
    linewidth: float | None
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
    )
    antialiased: bool | None
    hatch: Literal['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'] | None
    fill: bool
    capstyle: Literal['butt', 'projecting', 'round'] | CapStyle
    joinstyle: Literal['miter', 'round', 'bevel'] | JoinStyle

class Patch(Artist):
    def __init__(self, **kwargs: Unpack[PatchArgs]) -> None: ...
    # TODO: more
    transform: Transform
    # TODO: more

class Shadow(Patch):
    def __init__(
        self,
        patch: Patch,
        ox: float,
        oy: float,
        props: Mapping[str, Any] = None,
        **kwargs: Unpack[PatchArgs],
    ) -> None: ...

class Rectangle(Patch):
    def __init__(
        self,
        xy: tuple[float, float],
        width: float,
        height: float,
        angle: float = 0.0,
        **kwargs: Unpack[PatchArgs],
    ) -> None: ...

class RegularPolygon(Patch): ...

class PathPatch(Patch):
    def __init__(self, path: Path, **kwargs: Unpack[PatchArgs]) -> None: ...

class StepPatch(PathPatch): ...

class Polygon(Patch):
    def __init__(
        self,
        xy: ArrayLike,
        closed: bool = True,
        **kwargs: Unpack[PatchArgs],
    ) -> None: ...

class Wedge(Patch): ...
class Arrow(Patch): ...
class FancyArrow(Polygon): ...
class CirclePolygon(RegularPolygon): ...

class Ellipse(Patch):
    def __init__(
        self,
        xy: tuple[float, float],
        width: float,
        height: float,
        angle: float = 0,
        **kwargs: Unpack[PatchArgs],
    ) -> None: ...

class Circle(Ellipse): ...
class Arc(Ellipse): ...

# TODO: styles

class FancyBboxPatch(Patch): ...
class FancyArrowPatch(Patch): ...
class ConnectionPatch(FancyArrowPatch): ...
