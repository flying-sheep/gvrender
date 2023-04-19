from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import Literal

from ._types import _FontSize, _FontStretch, _FontWeight

class FontProperties:
    def __init__(
        self,
        family: str | Sequence[str] | None = None,
        style: Literal['normal', 'italic', 'oblique'] | None = None,
        variant: Literal['normal', 'small-caps'] | None = None,
        weight: _FontWeight | int | None = None,
        stretch: _FontStretch | int | None = None,
        size: _FontSize | int | None = None,
        fname: str | Path | None = None,  # if set, it's a hardcoded filename to use
        math_fontfamily: Literal['dejavusans', 'dejavuserif', 'cm', 'stix', 'stixsans', 'custom']
        | None = None,
    ) -> None: ...
