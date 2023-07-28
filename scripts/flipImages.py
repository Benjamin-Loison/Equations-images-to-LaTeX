import os
import shlex
from PIL import Image

path = 'C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\ENS\\Saclay\\M1\\DeepLearning\\Project\\Equations-images-to-LaTeX\\'

os.chdir(path)

def exec(cmd):
    os.system(cmd)

commonFolder = 'TestEM2014GTRGBNoLegendWhiteBlackCrop'
sourceFolder = f'{commonFolder}/'
destinationFolder = f'{commonFolder}Flip/'

def work(file):
    filePath = sourceFolder + file
    cmd = f'convert -flip {shlex.quote(filePath)} {shlex.quote(destinationFolder + file)}'
    print(cmd)
    exec(cmd)

for _, _, files in os.walk(sourceFolder):
    for file in files:
        work(file)

