from matplotlib.artist import Artist
from matplotlib.collections import Collection
from matplotlib.image import AxesImage
from matplotlib.legend import Legend
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle
from matplotlib.text import Text

class Axes:
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
    def add_artist(self, a: Artist): ...

class Axis(Artist): ...
class XAxis(Axis): ...
class YAxis(Axis): ...
