from __future__ import annotations

from collections.abc import Collection
from typing import Any, Literal, overload

from matplotlib.artist import Artist
from matplotlib.collections import Collection as MPLCollection
from matplotlib.container import Container
from matplotlib.image import AxesImage
from matplotlib.legend import Legend
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle
from matplotlib.table import Table
from matplotlib.text import Text

class _AxesBase(Artist):
    # adding artists
    def add_artist(self, a: Artist) -> Artist: ...
    def add_child_axes(self, ax: Axes) -> Axes: ...
    def add_collection(self, collection: MPLCollection, autolim: bool = True) -> MPLCollection: ...
    def add_container(self, container: Container) -> Container: ...
    def add_image(self, image: AxesImage) -> AxesImage: ...
    def add_line(self, line: Line2D) -> Line2D: ...
    def _add_text(self, txt: Text) -> Text: ...
    def add_patch(self, p: Patch) -> Patch: ...
    def add_table(self, tab: Table) -> Table: ...
    # xlim
    def get_xlim(self) -> tuple[float, float]: ...
    @overload
    def set_xlim(
        self,
        left: float | None = None,
        right: float | None = None,
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
        xmin: float | None = None,
        xmax: float | None = None,
        emit: bool = True,
        auto: bool = False,
    ) -> tuple[float, float]: ...
    # ylim
    def get_ylim(self) -> tuple[float, float]: ...
    @overload
    def set_ylim(
        self,
        bottom: float | None = None,
        top: float | None = None,
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
        ymin: float | None = None,
        ymax: float | None = None,
        emit: bool = True,
        auto: bool = False,
    ) -> tuple[float, float]: ...
    # TODO: more
    def get_aspect(self) -> Literal['auto'] | float: ...
    def set_aspect(
        self,
        aspect: Literal['auto', 'equal'] | float,
        adjustable: Literal['box', 'datalim'] | None = None,
        anchor: str | tuple[float, float] | None = None,
        share: bool = False,
    ) -> None: ...
    # TODO: more

class Axes(_AxesBase):
    artists: list[Artist]
    patch: Rectangle
    collections: list[MPLCollection]
    images: list[AxesImage]
    legends: list[Legend]
    lines: list[Line2D]
    patches: list[Patch]
    texts: list[Text]
    xaxis: XAxis
    yaxis: YAxis
    @overload
    def axis(
        self,
        option: (
            tuple[float, float, float, float]
            | bool
            | Literal['on', 'off', 'equal', 'scaled', 'tight', 'auto', 'image', 'square']
        ),
        *,
        emit: bool = True,
    ) -> tuple[float, float, float, float]: ...
    @overload
    def axis(
        self,
        *,
        xmin: float | None = None,
        xmax: float | None = None,
        ymin: float | None = None,
        ymax: float | None = None,
        emit: bool = True,
    ) -> tuple[float, float, float, float]: ...
    def get_title(self, loc="center") -> str: ...
    def set_title(self, label, fontdict=None, loc=None, pad=None, *, y=None, **kwargs) -> Text: ...
    def get_legend_handles_labels(self, legend_handler_map=None) -> tuple[Any, Any]: ...
    @overload
    def legend(self, labels: Collection[str] = ()) -> Legend: ...
    @overload
    def legend(self, handles: Collection[Artist], labels: Collection[str]) -> Legend: ...
    # TODO ...

class Axis(Artist): ...
class XAxis(Axis): ...
class YAxis(Axis): ...
