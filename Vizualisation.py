#!/usr/bin/env python3
import sys
import os
from numpy import genfromtxt


from HistogramViz import HistogramViz
from ScatterViz import ScatterViz


def get_name_csv():
    dir = os.listdir('./')
    for x in range(0, len(dir)):
        if len(dir[x]) > 4 and dir[x][len(dir[x]) - 4:len(dir[x])] == ".csv":
            return dir[x]
    return ""


def getDataWithType(data, type):
    newData = []
    for i in range(1, len(data)):
        cmp = data[i][3].replace('"', '')
        if type == 1 and cmp == "M":
            newData.append(data[i])

        elif type == 2 and cmp == "F":
            newData.append(data[i])
    return newData


if __name__ == "__main__":
    file_data = get_name_csv()
    if file_data == "":
        print("No csv found")
        sys.exit(42)
    print("Found DataFile %s" % file_data)
    try:
        data = genfromtxt(file_data, delimiter=",", dtype="|U", autostrip=True)
        print("Read DataFile %s" % file_data)
    except IOError as e:
        print(str(e))
        sys.exit(42)
    print("What type do you want ?")
    print("Only Male : press M")
    print("Only Female : press F")
    print("All : Any other key")
    type = input("Please enter any Key : ").split(' ')[0]
    flag = "all"
    if type.upper() == "M":
        print("Loading male data")
        data = getDataWithType(data, 1)
        flag = "man"
    elif type.upper() == "F":
        print("Loading female data")
        data = getDataWithType(data, 2)
        flag = "female"

    print("Parsing dataFile %s" % file_data)
    ScatterViz(data, flag)
    HistogramViz(data, flag)
    sys.exit(0)
