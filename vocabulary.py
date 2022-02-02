import os

path = 'C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\ENS\\Saclay\\M1\\DeepLearning\\Project\\im2latex\\processed\\'

os.chdir(path)

f = open('im2latex_formulas.norm.lst')
lines = f.read().splitlines()
f.close()

sentences = []

startWord = 'start'
endWord = 'end'
padWord = 'pad'

wordsToIndexes = {}
indexesToWords = {}
wordsCount = {}

# to force these special words to have indexes 0, 1 and 2
for word in [startWord, endWord, padWord]:
    index = len(wordsToIndexes)
    wordsToIndexes[word] = index
    indexesToWords[index] = word

for line in lines:
    words = line.split()
    words = list(filter(('\\,').__ne__, words))
    for word in words:
        if not word in wordsToIndexes:
            index = len(wordsToIndexes)
            wordsToIndexes[word] = index
            indexesToWords[index] = word
            wordsCount[word] = 0
        wordsCount[word] += 1

    words = [startWord] + words + [endWord]
    words = [wordsToIndexes[word] for word in words]

    sentences += [words]

wordsCount = {k: v for k, v in sorted(wordsCount.items(), key=lambda item: item[1])}
for word in wordsCount:
    print(word, wordsCount[word])

