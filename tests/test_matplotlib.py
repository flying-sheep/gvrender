"""Matplotlib rendering tests"""

import pytest
from matplotlib import pyplot

from gvrender.matplotlib import render

MIN_DOT = 'graph { a -- b }'


@pytest.mark.mpl_image_compare
def test_render():
    """A simple render call should work"""
    fig, axes = pyplot.subplots()
    axes.set_aspect('equal')
    render(MIN_DOT, axes, prog='dot')
    return fig
