#! /usr/bin/python3

# %%
from bokeh.layouts import column
from bokeh.models import Range1d
import numpy as np
from typing import Tuple, List
from bokeh.plotting.figure import Figure

from util import graph


def get_data() -> Tuple[List[int], List[int]]:
    x = np.linspace(0, 4 * np.pi, 100)
    y = np.sin(x)
    return (x, y)


def make_graph() -> Figure:
    x: List[int]
    y: List[int]
    x, y = get_data()
    TOOLS: str = "pan,wheel_zoom,box_zoom,reset,save,box_select"
    title: str = "Legend Example"

    p1: Figure = graph.make_figure(
        title=title, tools=TOOLS, x_range=Range1d(0, 10))
    graph.circle(p1, x, y, legend='sin(x)')
    graph.circle(p1, x, 2 * y, legend='2*sin(x)', color='orange')
    graph.circle(p1, x, 3 * y, legend='3*sin(x)', color='green')

    figure = make_range_tool(p1)

    return column(p1, figure)


def make_range_tool(p: Figure) -> Figure:
    return graph.set_range_tool(p)


graph.show_figure(make_graph())
