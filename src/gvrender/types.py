"""Reused types"""

from __future__ import annotations

from typing import Literal

from pygraphviz import AGraph

Prog = Literal['neato', 'dot', 'twopi', 'circo', 'fdp', 'nop']
GraphLike = AGraph | str | bytes
