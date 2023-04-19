from __future__ import annotations

from matplotlib.artist import Artist
from matplotlib.cm import ScalarMappable

class _ImageBase(Artist, ScalarMappable): ...
class AxesImage(_ImageBase): ...
