import os
from PIL import Image

path = 'C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\ENS\\Saclay\\M1\\DeepLearning\\Project\\im2latex\\processed\\formula_images_processed\\'

os.chdir(path)

size = 800
# checked on all images
# also checked that all files are images

xMin, xMax, yMin, yMax = size - 1, 0, size - 1, 0

def work(fileName):
    global xMin, xMax, yMin, yMax
    im = Image.open(fileName)
    pix = im.load()
    width, height = im.size

    """for y in range(0, min(yMin, height)):
        for x in range(width):
            if pix[x, y] != 255:
                if y < yMin:
                    yMin = y"""
    xMaxChanged = False
    yMaxChanged = False
    localMinX, localMinY = width - 1, height - 1
    for y in range(height):
        for x in range(width):
            if pix[x, y] != (255, 255, 255):
                """if x < localMinX:
                    localMinX = x
                if y < localMinY:
                    localMinY = y"""
                if x < xMin:
                    xMin = x
                if x > xMax:
                    xMax = x
                    xMaxChanged = True
                if y < yMin:
                    yMin = y
                if y > yMax:
                    yMax = y
                    yMaxChanged = True
    #if localMinX != 1 or localMinY != 1:
    #    print(f'/!\\ different min {fileName} {localMinX,localMinY} /!\\')
    if xMaxChanged:
        print(f'new xMax {fileName} {xMax}')
    if yMaxChanged:
        print(f'new yMax {fileName} {yMax}')

for r, d, files in os.walk('.'):
    filesLen = len(files)
    for filesIndex in range(filesLen):
        file = files[filesIndex]
        if filesIndex % 1000 == 0:
            print(f'{filesIndex} / {filesLen}: {file} {xMin, xMax, yMin, yMax}')
        work(file)