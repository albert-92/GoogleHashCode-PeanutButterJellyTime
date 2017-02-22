def readAndParseInputFile(filePath):
    lines = []

    with open(filePath) as f:
        lines = [line.rstrip('\n') for line in f]

    firstLineSplittet = lines.pop(0).split()

    parsedData = {
        'rows': firstLineSplittet[0],
        'columns': firstLineSplittet[1],
        'minIngredientPerSlice': firstLineSplittet[2],
        'maxCellsPerSlice': firstLineSplittet[3]
    }

    pizza = []

    for line in lines:
        pizza.append(list(line))

    return parsedData, pizza


