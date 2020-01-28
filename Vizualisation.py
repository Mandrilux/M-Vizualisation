#!/usr/bin/env python3
import sys
import os
import plotly.graph_objects as go
from numpy import genfromtxt, array
import plotly.io as pio
import statsmodels.api as sm
from ScatterViz import ScatterViz


def get_name_csv():
    dir = os.listdir('./')
    for x in range(0, len(dir)):
        if len(dir[x]) > 4 and dir[x][len(dir[x]) - 4:len(dir[x])] == ".csv":
            return dir[x]
    return ""

def getDateWithType(data , type):
    
    return data

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
    print ("What type do you want ?")
    print ("Only man : press M")
    print ("Only girl : press F")
    print ("All : Any key")
    type = input("Please enter any Key : ").split(' ')[0]
    print (type)

    if type == "H":
        print ("Loading man data")
        data = getDateWithType(data, 1)
    elif type == "F":
        print ("Loading female data")
        data = getDateWithType(data, 2)

    print("Parsing dataFile %s" % file_data)
    ScatterViz(data)
    sys.exit(0)
