from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from matplotlib.axes import Axes
from matplotlib.figure import Figure

def gcf() -> Figure: ...
def gca() -> Axes: ...
def subplots(
    nrows: int = 1,
    ncols: int = 1,
    sharex: bool = False,
    sharey: bool = False,
    squeeze: bool = True,
    subplot_kw: Mapping[str, Any] = None,
    gridspec_kw: Mapping[str, Any] = None,
    **fig_kw,
) -> tuple[Figure, Axes | list[Axes]]: ...
