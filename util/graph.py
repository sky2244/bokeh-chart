
from bokeh.io import show, output_notebook
from bokeh.plotting import figure
from bokeh.plotting.figure import Figure
from typing import List, Union

Real = Union[int, float]


def make_figure(title: str, **kargs) -> Figure:
    return figure(title=title, **kargs)


def circle(p: Figure, x: List[Real], y: List[Real], **kargs) -> None:
    p.circle(x, y, **kargs)


def show_figure(p: Figure) -> None:
    output_notebook()
    show(p)
