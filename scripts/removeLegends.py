import os
import shlex

path = 'C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\ENS\\Saclay\\M1\\DeepLearning\\Project\\Equations-images-to-LaTeX\\'

os.chdir(path)

def exec(cmd):
    os.system(cmd)

sourceFolder = 'TestEM2014GTRGB'
destinationFolder = sourceFolder + 'NoLegend'

#sourceFolder = 'TestEM2014GTRGBNoLegend'
#destinationFolder = sourceFolder + 'Crop'

for _, _, files in os.walk(folder):
    for file in files:
        filePath = folder + '/' + file
        fileName = file.split('.')[0]
        cmd = f'convert {shlex.quote(filePath)} -fill white +opaque "#284054" {shlex.quote(f"{destinationFolder}/{fileName}.png")}'
        exec(cmd)

