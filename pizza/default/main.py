from pizza.default.fileInput import readAndParseInputFile
import math

inputPath = '../input/'

exampleFile = inputPath + 'example.in'
smallFile = inputPath + 'small.in'
mediumFile = inputPath + 'medium.in'
bigFile = inputPath + 'big.in'

info, pizza = readAndParseInputFile(exampleFile)

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