#!/usr/bin/python3

import os
import shlex

#path = 'C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\ENS\\Saclay\\M1\\DeepLearning\\Project\\Equations-images-to-LaTeX\\'

#os.chdir(path)

def exec(cmd):
    #print(cmd)
    os.system(cmd)

folder = 'TestEM2014GT'

for _, _, files in os.walk(folder):
    for file in files:
        filePath = folder + '/' + file
        fileName = file.split('.')[0]
        cmd = f'python3 inkml2img.py {shlex.quote(filePath)} {shlex.quote(f"{folder}RGB/{fileName}.png)}'
        exec(cmd)

