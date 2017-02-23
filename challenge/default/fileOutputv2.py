def parseAndSaveOutputFile(caches: list, outputFilePath):
    with open(outputFilePath, 'w') as f:
        f.write(str(len(caches)))
        f.write('\n')

        i = 0

        for cache in caches:
            f.write(str(i) + ' ')
            f.write(' '.join(map(str, cache)))
            f.write('\n')

            i += 1

