from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.transform import Transform


class Artist:
    figure: Figure
    axes: Axes
    def set_transform(self, t: Transform): ...
    def get_transform(self) -> Transform: ...
    def is_transform_set(self) -> bool: ...
