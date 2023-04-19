from pathlib import Path
from typing import Literal, Optional, Sequence, Union

from ._types import _FontSize, _FontStretch, _FontWeight


class FontProperties:
    def __init__(
        self,
        family: Union[str, Sequence[str], None] = None,
        style: Optional[Literal['normal', 'italic', 'oblique']] = None,
        variant: Optional[Literal['normal', 'small-caps']] = None,
        weight: Union[_FontWeight, int, None] = None,
        stretch: Union[_FontStretch, int, None] = None,
        size: Union[_FontSize, int, None] = None,
        fname: Union[str, Path, None] = None,  # if set, it's a hardcoded filename to use
        math_fontfamily: Optional[
            Literal['dejavusans', 'dejavuserif', 'cm', 'stix', 'stixsans', 'custom']
        ] = None,
    ) -> None: ...
