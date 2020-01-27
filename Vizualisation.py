#!/usr/bin/env python3
import sys
import csv
import os
from numpy import genfromtxt


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
        data = genfromtxt(file_data, delimiter=',')
    except IOError as e :
        print (str(e))
        sys.exit(42)
    sys.exit(0)
