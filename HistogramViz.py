import plotly.express as px

from DataProcessing import FormatData


def HistogramViz(data, flag):
    format_data = FormatData(data)

    print("Generate graph : please wait")
    fig = px.histogram(format_data, x="age", y="size", color="place", marginal="box")

    name_file = "histogram_" + flag + ".html"
    fig.write_html(name_file, auto_open=True)
