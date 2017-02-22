from pizza.default.fileInput import readAndParseInputFile

inputPath = '../input/'

exampleFile = inputPath + 'example.in'
smallFile = inputPath + 'small.in'
mediumFile = inputPath + 'medium.in'
bigFile = inputPath + 'big.in'

info, pizza = readAndParseInputFile(exampleFile)

print(info)
print(pizza)