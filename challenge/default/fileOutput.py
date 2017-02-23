def parseAndSaveOutputFile(caches: list, outputFilePath):
    with open(outputFilePath, 'w') as f:
        f.write(str(len(caches)))
        f.write('\n')

        for cache in caches:
            f.write(str(len(cache)))
            f.write(' '.join(map(str, cache)))
            f.write('\n')

