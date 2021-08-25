"""Matplotlib rendering tests"""

# from typing import get_type_hints
from matplotlib import pyplot
from pygraphviz import AGraph

from gvrender.matplotlib import render

MIN_DOT = 'graph { a -- b }'


# def test_get_json():
#     got = _get_render_data(AGraph(string=min_dot), prog='dot')
#     assert got.keys() == get_type_hints(xdot.Graph).keys()


def test_render():
    """A simple render call should work"""
    fig, axes = pyplot.subplots()
    render(AGraph(string=MIN_DOT), axes, prog='dot')
    fig.show()
