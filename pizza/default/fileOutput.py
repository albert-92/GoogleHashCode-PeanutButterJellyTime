def parseAndSaveOutputFile(slices: list, outputFilePath):
    with open(outputFilePath, 'w') as f:
        f.write(str(len(slices)))
        f.write('\n')

        for slice in slices:
            f.write(' '.join(slice))
            f.write('\n')

