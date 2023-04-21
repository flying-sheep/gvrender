"""Reused types"""

from __future__ import annotations

from typing import Literal, Union

from pygraphviz import AGraph

Prog = Literal['neato', 'dot', 'twopi', 'circo', 'fdp', 'nop']
GraphLike = Union[AGraph, str, bytes]
