#! /usr/bin/python3

# %%
import numpy as np
from bokeh.io import show, output_notebook
from bokeh.plotting import figure, show


def get_data():
    x = np.linspace(0, 4 * np.pi, 100)
    y = np.sin(x)
    return (x, y)


def make_figure():
    x, y = get_data()
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

    p1 = figure(title="Legend Example sample", tools=TOOLS)
    p1.circle(x, y, legend="sin(x)")
    p1.circle(x, 2 * y, legend="2*sin(x)", color="orange")
    p1.circle(x, 3 * y, legend="3*sin(x)", color="green")

    return p1


output_notebook()
show(make_figure())
