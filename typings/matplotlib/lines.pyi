import collections.abc as cabc
from typing import Optional

from matplotlib.artist import Artist

from ._types import _Color

class Line2D(Artist):
    def __init__(
        self,
        xdata: cabc.Collection[float],
        ydata: cabc.Collection[float],
        linewidth=None,  # all Nones default to rc
        linestyle=None,
        color: Optional[_Color] = None,
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
        **kwargs
    ) -> None: ...
