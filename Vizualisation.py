#!/usr/bin/env python3
import sys
import csv
import os
import plotly.graph_objects as go
from numpy import genfromtxt
from io import StringIO


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

    age_range = 16

    for l in range(1, len(data)):
        li = data[l]
        if int(li[2]) > age_range:
            age_range = int(li[2])

    format_data = []
    municipalites = []

    for lin in range(1, len(data)):
        line = data[lin]
        if line[7] in municipalites:
            line_index = municipalites.index(line[7])
            print(int(line[2]), age_range)
            format_data[line_index][int(line[2]) - 1] += 1
        else:
            municipalites.append(line[7])
            format_data.append([0] * age_range)

    ages = []
    for ind in range(16, age_range):
        ages.append(ind)

    fig = go.Figure(data=go.Heatmap(
        z=format_data,
        x=ages,
        y=municipalites,
        hoverongaps=False))
    fig.show()
    sys.exit(0)
