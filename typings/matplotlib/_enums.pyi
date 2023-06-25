from __future__ import annotations

from enum import Enum

class CapStyle(str, Enum):
    butt = 'butt'
    projecting = 'projecting'
    round = 'round'

class JoinStyle(str, Enum):
    miter = 'miter'
    round = 'round'
    bevel = 'bevel'
