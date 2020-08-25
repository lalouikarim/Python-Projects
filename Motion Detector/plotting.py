import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
from motion_detector import df
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

column_data_source = ColumnDataSource(df)

f = figure(height = 100, width = 500, x_axis_type = "datetime", title = "Motion Graph", sizing_mode = 'scale_width')
f.yaxis.minor_tick_line_color = None

hover = HoverTool(tooltips = [("Start", "@Start_string"), ("End", "@End_string")])
f.add_tools(hover)

f.quad(top = 1, bottom = 0, left = "Start", right = "End", color = "green", source = column_data_source)

output_file("Motion Detector.html")

show(f)