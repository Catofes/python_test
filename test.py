#!/bin/python

from scipy import interpolate
import sys

if __name__ == '__main__':
    file = open("a.out", "r")
    data = {}
    for line in file:
        line = " ".join(filter(lambda x: x, line.split(" ")))
        result = line.split(" ")
        energy = float(result[0])
        if result[1] == 'keV':
            energy /= 1000
        dedx = float(result[2]) + float(result[3])
        data[energy] = dedx

    sorted(data)

    x = list(data.keys())
    y = list(data.values())

    linear = interpolate.interp1d(x, y, kind='cubic')
    print(linear(float(sys.argv[1])))
