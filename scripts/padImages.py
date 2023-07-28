import os
import shlex

path = 'C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\ENS\\Saclay\\M1\\DeepLearning\\Project\\im2latex\\processed\\'

os.chdir(path)

def exec(cmd):
    os.system(cmd)

commonFolder = 'formula_images_processed'
sourceFolder = f'{commonFolder}\\'
destinationFolder = f'{commonFolder}_padded\\'

def work(file):
    filePath = sourceFolder + file
    cmd = f'convert {shlex.quote(filePath)} -gravity NorthWest -background white -extent 800x800 {shlex.quote(destinationFolder + file)}'
    exec(cmd)

for r, d, files in os.walk(sourceFolder):
    filesLen = len(files)
    for filesIndex in range(filesLen):
        file = files[filesIndex]
        if filesIndex % 1000 == 0:
            print(f'{filesIndex} / {filesLen}')
        work(file)
