import collections.abc as cabc
from typing import Any, Optional, Union, overload

from matplotlib.artist import Artist
from matplotlib.collections import Collection
from matplotlib.image import AxesImage
from matplotlib.legend import Legend
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle
from matplotlib.text import Text

class _AxesBase(Artist):
    def add_artist(self, a: Artist): ...
    # xlim
    def get_xlim(self) -> tuple[float, float]: ...
    @overload
    def set_xlim(
        self,
        left: Optional[float] = None,
        right: Optional[float] = None,
        emit: bool = True,
        auto: bool = False,
    ) -> tuple[float, float]: ...
    @overload
    def set_xlim(
        self, lr: tuple[float, float] = None, /, *, emit: bool = True, auto: bool = False
    ) -> tuple[float, float]: ...
    @overload
    def set_xlim(
        self,
        *,
        xmin: Optional[float] = None,
        xmax: Optional[float] = None,
        emit: bool = True,
        auto: bool = False,
    ) -> tuple[float, float]: ...
    # ylim
    def get_ylim(self) -> tuple[float, float]: ...
    @overload
    def set_ylim(
        self,
        bottom: Optional[float] = None,
        top: Optional[float] = None,
        emit: bool = True,
        auto: bool = False,
    ) -> tuple[float, float]: ...
    @overload
    def set_ylim(
        self, bt: tuple[float, float] = None, *, emit: bool = True, auto: bool = False
    ) -> tuple[float, float]: ...
    @overload
    def set_ylim(
        self,
        *,
        ymin: Optional[float] = None,
        ymax: Optional[float] = None,
        emit: bool = True,
        auto: bool = False,
    ) -> tuple[float, float]: ...

class Axes(_AxesBase):
    artists: list[Artist]
    patch: Rectangle
    collections: list[Collection]
    images: list[AxesImage]
    legends: list[Legend]
    lines: list[Line2D]
    patches: list[Patch]
    texts: list[Text]
    xaxis: XAxis
    yaxis: YAxis
    def get_title(self, loc="center") -> str: ...
    def set_title(self, label, fontdict=None, loc=None, pad=None, *, y=None, **kwargs) -> Text: ...
    def get_legend_handles_labels(self, legend_handler_map=None) -> tuple[Any, Any]: ...
    @overload
    def legend(self, labels: cabc.Collection[str] = ()) -> Legend: ...
    @overload
    def legend(self, handles: cabc.Collection[Artist], labels: cabc.Collection[str]) -> Legend: ...
    # TODO ...

class Axis(Artist): ...
class XAxis(Axis): ...
class YAxis(Axis): ...
