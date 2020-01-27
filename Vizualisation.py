#!/usr/bin/env python3
import sys
import csv
from numpy import genfromtxt


if __name__ == "__main__":
    data = genfromtxt('data.csv', delimiter=',')
    print ("ok")
    sys.exit(0)
