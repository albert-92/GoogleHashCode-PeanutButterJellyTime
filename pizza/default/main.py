from pizza.default.fileInput import *
from pizza.default.fileOutput import *
import math

inputPath = '../input/'
outputPath = './output/'

exampleFile = 'example'
smallFile = 'small'
mediumFile = 'medium'
bigFile = 'big'

currentFile = exampleFile

info, pizza = readAndParseInputFile(inputPath + currentFile + '.in')

print(info)
print(pizza)

size = math.floor(math.sqrt(int(info['maxCellsPerSlice'])))

slices = []

for x in range(0, int(info['rows'])-size+1, size):
    for y in range(0, int(info['columns'])-size+1, size):
        xend = x+size
        yend = y+size
        slices.append([x, y, xend, yend])

print(slices)

parseAndSaveOutputFile(slices, outputPath + currentFile + '.out')