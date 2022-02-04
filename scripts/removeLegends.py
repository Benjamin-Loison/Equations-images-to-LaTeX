import os

path = 'C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\ENS\\Saclay\\M1\\DeepLearning\\Project\\Equations-images-to-LaTeX\\'

os.chdir(path)

def exec(cmd):
    os.system(cmd)

sourceFolder = 'TestEM2014GTRGB'
destinationFolder = 'TestEM2014GTRGBNoLegend'

#sourceFolder = 'TestEM2014GTRGBNoLegend'
#destinationFolder = 'TestEM2014GTRGBNoLegendCrop'

for r, d, files in os.walk(folder):
    for file in files:
        filePath = folder + '/' + file
        fileName = file.split('.')[0]
        cmd = 'convert ' + filePath + ' -fill white +opaque "#284054" ' + destinationFolder + '/' + fileName + '.png'
        exec(cmd)

