from __future__ import annotations

from collections.abc import Collection

from matplotlib.artist import Artist

from ._types import _Color

class Line2D(Artist):
    def __init__(
        self,
        xdata: Collection[float],
        ydata: Collection[float],
        linewidth=None,  # all Nones default to rc
        linestyle=None,
        color: _Color | None = None,
        marker=None,
        markersize=None,
        markeredgewidth=None,
        markeredgecolor=None,
        markerfacecolor=None,
        markerfacecoloralt='none',
        fillstyle=None,
        antialiased=None,
        dash_capstyle=None,
        solid_capstyle=None,
        dash_joinstyle=None,
        solid_joinstyle=None,
        pickradius: int = 5,
        drawstyle=None,
        markevery=None,
        **kwargs,
    ) -> None: ...
