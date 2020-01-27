#!/usr/bin/env python3
import sys
import os
import plotly.graph_objects as go
from numpy import genfromtxt, array
import plotly.express as px
import plotly.io as pio
import statsmodels.api as sm

pio.renderers.default = "browser"


def get_name_csv():
    dir = os.listdir('./')
    for x in range(0, len(dir)):
        if len(dir[x]) > 4 and dir[x][len(dir[x]) - 4:len(dir[x])] == ".csv":
            return dir[x]
    return ""


if __name__ == "__main__":
    file_data = get_name_csv()
    print("Found DataFile %s" % file_data)
    try:
        data = genfromtxt(file_data, delimiter=",", dtype="|U", autostrip=True)
    except IOError as e:
        print(str(e))
        sys.exit(42)

    format_data = [{}] * (len(data) - 1)

    for lin in range(1, len(data)):
        line = data[lin]
        format_data[lin - 1] = {
            "place": line[7],
            "age": int(line[2]),
            "size": 50
        }

    for lin in range(1, len(data)):
        line = data[lin]
        format_data[lin - 1]["size"] = len([x for x in format_data if x.get("age") == format_data[lin - 1]["age"]])

    fig = px.scatter(format_data, x="age", y="place", color="place", opacity=0.1, size="size")

    fig.write_html('tmp.html', auto_open=True)

    sys.exit(0)
