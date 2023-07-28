import os
import shlex
from PIL import Image

path = 'C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\ENS\\Saclay\\M1\\DeepLearning\\Project\\Equations-images-to-LaTeX\\'

os.chdir(path)

def exec(cmd):
    os.system(cmd)

commonFolder = 'TestEM2014GTRGBNoLegendWhiteBlack'
sourceFolder = f'{commonFolder}/'
destinationFolder = f'{commonFolder}Crop/'

def work(file):
    filePath = sourceFolder + file
    im = Image.open(filePath)
    pix = im.load()
    width, height = im.size

    xMin, xMax, yMin, yMax = width - 1, 0, height - 1, 0

    for y in range(height):
        for x in range(width):
            if pix[x, y] != 255:
                if x < xMin:
                    xMin = x
                if x > xMax:
                    xMax = x
                if y < yMin:
                    yMin = y
                if y > yMax:
                    yMax = y

    #print(xMin, xMax, yMin, yMax)
    deltaX, deltaY = xMax - xMin + 1, yMax - yMin + 1
    cmd = f'convert {shlex.quote(filePath)} -crop {deltaX}x{deltaY}+{xMin)+{yMin} {shlex.quote(destinationFolder + file)}'
    print(cmd)
    exec(cmd)

for _, _, files in os.walk(sourceFolder):
    for file in files:
        work(file)

