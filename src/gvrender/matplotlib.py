"""

References
----------

- `Artists tutorial`_

.. _artists tutorial: https://matplotlib.org/stable/tutorials/intermediate/artists.html
"""

from __future__ import annotations

from collections.abc import Iterable

import xdot_rs
import xdot_rs.shapes as xs
from matplotlib.axes import Axes
from matplotlib.font_manager import FontProperties
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse, PathPatch
from matplotlib.path import Path
from matplotlib.text import Text
from pygraphviz import AGraph

from .types import GraphLike, Prog


def render(graph_or_code: GraphLike, axes: Axes | None = None, *, prog: Prog | None = None):
    """Render a graph to matplotlib"""
    if axes is None:
        from matplotlib import pyplot

        axes = pyplot.gca()

    graph = to_xdot(graph_or_code, prog)
    draw(graph, axes)


def to_xdot(graph_or_code: GraphLike, prog: Prog | None) -> AGraph:
    """Convert an AGraph or Graphviz code to a xdot Graph"""
    if isinstance(graph_or_code, AGraph):
        graph = graph_or_code
    else:
        code = graph_or_code if isinstance(graph_or_code, str) else graph_or_code.decode('utf-8')
        graph = AGraph(string=code)
    if prog:
        graph = AGraph(string=graph.draw(format='xdot', prog=prog).decode('utf-8'))
    if not all('_draw_' in n.attr for n in graph.nodes_iter()):
        raise ValueError('You need to either specify `prog` or pass in a layouted graph')
    return graph


def draw(graph: AGraph, axes: Axes):
    """Draw an xdot graph into axes"""
    # x_a, y_a, x_b, y_b = graph.bounding
    # axes.set_xlim(x_a, x_b)
    # axes.set_ylim(y_a, y_b)

    edge_shapes = [
        shape
        for edge in graph.edges_iter()
        for shape in xdot_rs.parse(
            (edge.attr.get('_draw_') or '') + (edge.attr.get('_ldraw_') or '')
        )
    ]
    node_shapes = [
        shape
        for node in graph.nodes_iter()
        for shape in xdot_rs.parse(
            (node.attr.get('_draw_') or '') + (node.attr.get('_ldraw_') or '')
        )
    ]
    # TODO: default is 'breadthfirst', not 'nodesfirst'
    if graph.graph_attr.get('outputorder') == 'edgesfirst':
        _draw_shapes(edge_shapes, axes)
        _draw_shapes(node_shapes, axes)
    else:
        _draw_shapes(node_shapes, axes)
        _draw_shapes(edge_shapes, axes)


def _draw_shapes(shapes: Iterable[xdot_rs.ShapeDraw], axes: Axes):
    for sd in shapes:
        color = (
            sd.pen.color.r / 255,
            sd.pen.color.g / 255,
            sd.pen.color.b / 255,
            sd.pen.color.a / 255,
        )
        if isinstance(sd.shape, xs.Ellipse):
            axes.add_patch(
                Ellipse(
                    (sd.shape.x, sd.shape.y),
                    sd.shape.w,
                    sd.shape.h,
                    edgecolor=color,
                    facecolor=sd.pen.fill_color if sd.shape.filled else '#0000',
                    linewidth=sd.pen.line_width,
                )
            )
        elif isinstance(sd.shape, xs.Points):
            x, y = zip(*sd.shape.points)
            if sd.shape.type == xs.PointsType.Polygon:
                axes.add_line(Line2D(x, y))
            elif sd.shape.type == xs.PointsType.BSpline:
                codes = [Path.MOVETO] + ([Path.CURVE4] * (len(sd.shape.points) - 1))
                axes.add_patch(
                    PathPatch(
                        Path(sd.shape.points, codes),
                        edgecolor=color,
                        linewidth=sd.pen.line_width,
                    )
                )
            else:
                assert False, f'Unhandled PointsType {sd.shape.type}'
        elif isinstance(sd.shape, xs.Text):
            font_props = FontProperties(
                family=sd.pen.font_name,
                style='italic' if sd.pen.font_characteristics.italic else 'normal',
                weight='bold' if sd.pen.font_characteristics.bold else 'normal',
                size=int(sd.pen.font_size),
            )
            axes._add_text(  # pylint: disable=protected-access
                Text(
                    sd.shape.x,
                    sd.shape.y,
                    sd.shape.text,
                    color=color,
                    fontproperties=font_props,
                )
            )
        else:
            assert False, f'Unhandled shape {sd.shape}'
