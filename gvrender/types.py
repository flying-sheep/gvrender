"""Reused types"""

from typing import Literal, Union

from pygraphviz import AGraph
from xdot.ui.elements import Graph

Prog = Literal['neato', 'dot', 'twopi', 'circo', 'fdp', 'nop']
GraphLike = Union[AGraph, Graph, str, bytes]
