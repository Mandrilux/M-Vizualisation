import plotly.express as px

from DataProcessing import FormatData


def ScatterViz(data, flag):
    format_data = FormatData(data)

    print("Generate graph : please wait")
    fig = px.scatter(format_data, x="age", y="size", color="place", opacity=0.5, size="size", trendline='lowess')

    name_file = "scatter_" + flag + ".html"
    fig.write_html(name_file, auto_open=True)
