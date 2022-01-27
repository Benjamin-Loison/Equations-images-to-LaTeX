#!/usr/bin/python3

import os

#path = 'C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\ENS\\Saclay\\M1\\DeepLearning\\Project\\Equations-images-to-LaTeX\\'

#os.chdir(path)

def exec(cmd):
    #print(cmd)
    os.system(cmd)

folder = 'TestEM2014GT'

for r, d, files in os.walk(folder):
    for file in files:
        filePath = folder + '/' + file
        fileName = file.split('.')[0]
        cmd = 'python3 inkml2img.py ' + filePath + ' ' + folder + 'RGB/' + fileName + '.png'
        exec(cmd)

