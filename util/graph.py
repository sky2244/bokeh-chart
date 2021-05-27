
from bokeh.io import show, output_notebook
from bokeh.plotting import figure
from bokeh.plotting.figure import Figure
from bokeh.models import RangeTool
from typing import List, Union, Dict, Any

Real = Union[int, float]


def make_figure(title: str, **kargs: Dict[str, Any]) -> Figure:
    return figure(title=title, **kargs)


def circle(p: Figure, x: List[Real], y: List[Real],
           **kargs: Dict[str, Any]) -> None:
    p.circle(x, y, **kargs)


def show_figure(p: Figure) -> None:
    output_notebook()
    show(p)


def set_range_tool(p: Figure, x_range: Any=None) -> Figure:
    if x_range is None:
        x_range = p.x_range
    range_tool = RangeTool(x_range=x_range)
    range_tool.overlay.fill_color = "navy"
    range_tool.overlay.fill_alpha = 0.2

    range_select = Figure(y_range=p.y_range, height=200)
    range_select.add_tools(range_tool)
    range_select.renderers = p.renderers

    return range_select
