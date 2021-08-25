import collections.abc as cabc
from typing import Any, Union

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
    subplot_kw: cabc.Mapping[str, Any] = None,
    gridspec_kw: cabc.Mapping[str, Any] = None,
    **fig_kw
) -> tuple[Figure, Union[Axes, list[Axes]]]: ...
