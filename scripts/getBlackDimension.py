import os
from PIL import Image

path = 'C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\ENS\\Saclay\\M1\\DeepLearning\\Project\\Equations-images-to-LaTeX\\'

os.chdir(path)

def work(fileName):
    im = Image.open(fileName)
    pix = im.load()
    width, height = im.size

    xMin, xMax, yMin, yMax = width - 1, 0, height - 1, 0

    for y in range(height):
        for x in range(width):
            if pix[x, y] != 0:
                if x < xMin:
                    xMin = x
                if x > xMax:
                    xMax = x
                if y < yMin:
                    yMin = y
                if y > yMax:
                    yMax = y

    xDelta, yDelta = xMax - xMin + 1, yMax - yMin + 1
    #print(xMin, xMax, yMin, yMax)
    #print(xDelta, yDelta)
    print(xDelta / yDelta)

folder = 'TestEM2014GTRGBNoLegend'

for r, d, files in os.walk(folder):
    for file in files:
        filePath = folder + '/' + file
        work(filePath)

