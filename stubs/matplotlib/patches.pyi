from matplotlib.artist import Artist
from matplotlib.path import Path

class Patch(Artist): ...

class PathPatch(Patch):
    def __init__(self, path: Path, **kwargs) -> None: ...
