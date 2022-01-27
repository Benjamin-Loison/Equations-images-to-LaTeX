#!/usr/bin/python3

import os

INFINITY = 65536

def work(fileName):
    f = open(fileName)
    lines = f.read().splitlines()
    f.close()

    xMin, xMax, yMin, yMax = INFINITY, 0, INFINITY, 0

    for line in lines:
        if line[0] != '<' and ', ' in line:
        #if ', ' in line:
            lineParts = line.split(', ')
            for linePart in lineParts:
                linePartParts = linePart.split()
                x, y = int(linePartParts[0]), int(linePartParts[1])
                if x < xMin:
                    xMin = x
                if x > xMax:
                    xMax = x
                if y < yMin:
                    yMin = y
                if y > yMax:
                    yMax = y

    #print(xMin, xMax, yMin, yMax)
    deltaX, deltaY = xMax - xMin, yMax - yMin
    print(deltaX, deltaY)

#fileName = '18_em_0.inkml'
#work(fileName)

folder = 'TestEM2014GT'

for r, d, files in os.walk(folder):
    for file in files:
        filePath = folder + '/' + file
        #print(filePath)
        work(filePath)
