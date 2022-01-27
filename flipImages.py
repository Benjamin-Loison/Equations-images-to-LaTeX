import os
from PIL import Image

path = 'C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\ENS\\Saclay\\M1\\DeepLearning\\Project\\Equations-images-to-LaTeX\\'

os.chdir(path)

def exec(cmd):
    os.system(cmd)

sourceFolder = 'TestEM2014GTRGBNoLegendWhiteBlackCrop/'
destinationFolder = 'TestEM2014GTRGBNoLegendWhiteBlackCropFlip/'

def work(file):
    filePath = sourceFolder + file
    cmd = 'convert -flip ' + filePath + ' ' + destinationFolder + file
    print(cmd)
    exec(cmd)

for r, d, files in os.walk(sourceFolder):
    for file in files:
        work(file)

