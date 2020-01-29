import plotly.express as px

from DataProcessing import FormatData


def ScatterViz(data, flag):
    format_data = FormatData(data)

    print("Generate graph : please wait")
    fig = px.scatter(format_data, x="age", y="place", color="place", opacity=0.1, size="size")

    name_file = "scatter_" + flag + ".html"
    fig.write_html(name_file, auto_open=True)
