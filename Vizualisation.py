#!/usr/bin/env python3
import sys
import csv
import os
import plotly.express as px
from numpy import genfromtxt
from io import StringIO

def get_name_csv():
    dir = os.listdir('./')
    for x in range(0, len(dir)):
        if len(dir[x]) > 4 and dir[x][len(dir[x]) - 4:len(dir[x])] == ".csv":
            return (dir[x])
    return ("")

if __name__ == "__main__":
    file_data = get_name_csv()
    print ("Found DataFile %s"% (file_data))
    try:
        data = genfromtxt(file_data, delimiter=",", dtype="|U", autostrip=True)
    except IOError as e :
        print (str(e))
        sys.exit(42)

    #print (data[1][1])
    """fig = px.imshow([[1, 20, 30],
                 [20, 1, 60],
                 [30, 60, 1],
                 [12, 17, 30]])
    fig.show()"""
    sys.exit(0)
