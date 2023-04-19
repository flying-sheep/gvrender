from pathlib import Path
from typing import Any, Literal, Union

from matplotlib.artist import Artist
from matplotlib.font_manager import FontProperties


class Text(Artist):
    def __init__(
        self,
        x: Union[int, float] = 0,
        y: Union[int, float] = 0,
        text: str = '',
        color=None,  # defaults to rc params
        verticalalignment='baseline',
        horizontalalignment='left',
        multialignment=None,
        fontproperties: Union[FontProperties, str, Path] = None,  # defaults to FontProperties()
        rotation=None,
        linespacing=None,
        rotation_mode=None,
        usetex=None,  # defaults to rcParams['text.usetex']
        wrap=False,
        transform_rotates_text=False,
        **kwargs,
    ) -> None: ...
    def get_rotation(self) -> float: ...
    def get_unitless_position(self) -> tuple[float, float]: ...
    def get_position(self) -> tuple[Any, Any]: ...  # TODO: type?
    def get_text(self) -> str: ...
    def set_x(self, x: Any) -> None: ...
    def set_y(self, y: Any) -> None: ...
    def set_rotation(self, s: Union[float, Literal['vertical', 'horizontal']]): ...
    def set_text(self, s: str) -> None: ...
    # TODO: there’s more
