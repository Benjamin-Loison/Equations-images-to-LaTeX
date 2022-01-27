import os
from PIL import Image

path = 'C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\ENS\\Saclay\\M1\\DeepLearning\\Project\\Equations-images-to-LaTeX\\'

os.chdir(path)

rMaxWidth, rMaxHeight = 0, 0

def preWork(file):
    global rMaxWidth, rMaxHeight
    filePath = sourceFolder + file
    im = Image.open(filePath)
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

    if xDelta > rMaxWidth: # same ratio otherwise wouldn't work
        rMaxWidth = xDelta
    if yDelta > rMaxHeight:
        rMaxHeight = yDelta

sourceFolder = 'TestEM2014GTRGBNoLegendWhiteBlackCropFlip/'
destinationFolder = 'TestEM2014GTRGBNoLegendWhiteBlackCropFlipSameSize/'

for r, d, files in os.walk(sourceFolder):
    for file in files:
        preWork(file)

print(rMaxWidth, rMaxHeight)

def work(file):
    filePath = sourceFolder + file
    im = Image.open(filePath)
    im = im.resize((rMaxWidth, rMaxHeight), Image.NEAREST)
    im.save(destinationFolder + file)

for r, d, files in os.walk(sourceFolder):
    for file in files:
        work(file)

