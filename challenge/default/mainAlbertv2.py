from challenge.default.fileInput import *
from challenge.default.fileOutput import *
import math

import numpy as np

import operator

inputPath = '../input/'
outputPath = './output/'

kittens = 'kittens'
me_at_the_zoo = 'me_at_the_zoo'
trending_today = 'trending_today'
videos_worth_spreading = 'videos_worth_spreading'

currentFile = kittens

# info, videos, endpoints, requests = readAndParseInputFile(inputPath + currentFile + '.in')

npArr = np.load(inputPath + currentFile + '.dump')

info = npArr[0]
videos = npArr[1]
endpoints = npArr[2]
requests = npArr[3]

print(info)
# print(videos)
# print(endpoints)
# print(requests)

# print(len(videos))
# print(len(endpoints))
# print(len(requests))

endpointVideoRanking = {}

# endpointVideoRanking = np.array(endpointVideoRanking)

for request in requests:
    Re = request['Re']
    Rv = request['Rv']
    Rn = request['Rn']

    if str(Re) in endpointVideoRanking:
        dict = endpointVideoRanking[str(Re)]
    else:
        dict = endpointVideoRanking[str(Re)] = {}

    if Rv in dict:
        dict[str(Rv)] += Rn
    else:
        dict[str(Rv)] = Rn

# print(endpointVideoRanking)

# endpointVideoRankingTemp = np.copy(endpointVideoRanking)

possibleCaches = []

for e in range(info['E']):
    endpointVideoRanking[str(e)] = sorted(endpointVideoRanking[str(e)].items(), key=operator.itemgetter(1),
    reverse=True)

    # print(endpointVideoRanking[str(e)])

    cacheVideos = []
    cacheSize = 0

    for video in endpointVideoRanking[str(e)]:
        if cacheSize + videos[int(video[0])] <= info['X']:
            cacheVideos.append(video[0])
            cacheSize += videos[int(video[0])]

    possibleCaches.append(cacheVideos)



chachesOutput = list(np.array(possibleCaches)[:info['C']])

parseAndSaveOutputFile(chachesOutput, outputPath + currentFile + '.out')


# print(endpointVideoRanking)

