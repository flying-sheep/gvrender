"""

References
----------

- `Artists tutorial`_

.. _artists tutorial: https://matplotlib.org/stable/tutorials/intermediate/artists.html
"""

import math
from typing import Iterable, Optional

from matplotlib.axes import Axes
from matplotlib.font_manager import FontProperties
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse, PathPatch
from matplotlib.path import Path
from matplotlib.text import Text
from pygraphviz import AGraph
from xdot.dot.parser import XDotParser
from xdot.ui import elements as xelem

from .types import GraphLike, Prog


def bounding(self):
    """hack to correctly infer bounding box: https://github.com/jrfonseca/xdot.py/issues/95"""
    x, w, j = self.x, self.w, self.j
    return x - 0.5 * (1 + j) * w, math.inf, x + 0.5 * (1 - j) * w, -math.inf


xelem.TextShape.bounding = property(bounding)  # type: ignore


def render(graph_or_code: GraphLike, axes: Optional[Axes] = None, *, prog: Optional[Prog] = None):
    """Render a graph to matplotlib"""
    if axes is None:
        from matplotlib import pyplot

        axes = pyplot.gca()

    graph = to_xdot(graph_or_code, prog)
    draw(graph, axes)


def to_xdot(graph_or_code: GraphLike, prog: Optional[Prog]) -> xelem.Graph:
    """Convert an AGraph or Graphviz code to a xdot Graph"""
    if isinstance(graph_or_code, xelem.Graph):
        graph = graph_or_code
    else:
        code = (
            graph_or_code
            if isinstance(graph_or_code, bytes)
            else str(graph_or_code).encode('utf-8')
        )
        if prog:
            code = AGraph(string=code.decode('utf-8')).draw(format='xdot', prog=prog)
        parser = XDotParser(code)
        graph = parser.parse()
    if not all(math.isfinite(b) for b in graph.bounding):
        raise ValueError('You need to either specify `prog` or pass in a layouted graph')
    return graph


def draw(graph: xelem.Graph, axes: Axes):
    """Draw an xdot graph into axes"""
    x_a, y_a, x_b, y_b = graph.bounding
    axes.set_xlim(x_a, x_b)
    axes.set_ylim(y_a, y_b)

    edge_shapes = [shape for edge in graph.edges for shape in edge.shapes]
    node_shapes = [shape for node in graph.nodes for shape in node.shapes]
    if graph.outputorder == 'edgesfirst':
        _draw_shapes(edge_shapes, axes)
        _draw_shapes(node_shapes, axes)
    else:
        _draw_shapes(node_shapes, axes)
        _draw_shapes(edge_shapes, axes)


def _draw_shapes(shapes: Iterable[xelem.Shape], axes: Axes):
    for shape in shapes:
        if isinstance(shape, xelem.LineShape):
            x, y = zip(*shape.points)
            axes.add_line(Line2D(x, y))
        elif isinstance(shape, xelem.BezierShape):
            codes = [Path.MOVETO] + ([Path.CURVE4] * (len(shape.points) - 1))
            axes.add_patch(
                PathPatch(
                    Path(shape.points, codes),
                    edgecolor=shape.pen.color,
                    linewidth=shape.pen.linewidth,
                )
            )
        elif isinstance(shape, xelem.TextShape):
            font_props = FontProperties(
                family=shape.pen.fontname,
                style='italic' if shape.pen.italic else 'normal',
                weight='bold' if shape.pen.bold else 'normal',
                size=int(shape.pen.fontsize),
            )
            axes._add_text(  # pylint: disable=protected-access
                Text(
                    shape.x,
                    shape.y,
                    shape.t,
                    color=shape.pen.color,
                    fontproperties=font_props,
                )
            )
        elif isinstance(shape, xelem.EllipseShape):
            axes.add_patch(
                Ellipse(
                    (shape.x0, shape.y0),
                    shape.w,
                    shape.h,
                    edgecolor=shape.pen.color,
                    facecolor=shape.pen.fillcolor if shape.filled else '#0000',
                    linewidth=shape.pen.linewidth,
                )
            )
        else:
            assert False, f'Unhandled shape {shape}'
