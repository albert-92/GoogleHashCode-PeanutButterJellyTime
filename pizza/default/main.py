from pizza.default.fileInput import *
from pizza.default.fileOutput import *
import math

inputPath = '../input/'
outputPath = './output/'

exampleFile = 'example'
smallFile = 'small'
mediumFile = 'medium'
bigFile = 'big'

currentFile = smallFile

info, pizza = readAndParseInputFile(inputPath + currentFile + '.in')

print(info)
print(pizza)

size = math.ceil(math.sqrt(int(info['maxCellsPerSlice'])))

slices = []
numSlices = 0

for x in range(0, int(info['rows'])-size+1, size):
    for y in range(0, int(info['columns'])-size+1, size):
        slices.append([x, x+size, y, y+size])
        numSlices += 1

print(numSlices)
print(slices)

parseAndSaveOutputFile(slices, outputPath + currentFile + '.out')