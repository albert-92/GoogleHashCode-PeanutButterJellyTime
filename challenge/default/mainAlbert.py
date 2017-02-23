from challenge.default.fileInput import *
from challenge.default.fileOutput import *
import math

import numpy as np

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

print(len(videos))
print(len(endpoints))
print(len(requests))

endpointVideoRanking = [[0] * info['V']] * info['E']

endpointVideoRanking = np.array(endpointVideoRanking)

for request in requests:
    Re = request['Re']
    Rv = request['Rv']
    Rn = request['Rn']

    endpointVideoRanking[Re, Rv] += Rn

# print(endpointVideoRanking)

endpointOutputs = []

for endpoint in endpointVideoRanking:

    endpointVideos = []
    endpointSize = 0

    full = False

    while endpointSize < info['X'] and np.count_nonzero(endpoint):
        if endpointSize + videos[np.argmax(endpoint)] < info['X']:
            endpointVideos.append(np.argmax(endpoint))
            endpointSize += videos[np.argmax(endpoint)]
            endpoint[np.argmax(endpoint)] = 0
        else:
            endpoint[np.argmax(endpoint)] = 0

    # print(endpoint)

    if endpointOutputs.__len__() < 500:
        endpointOutputs.append(endpointVideos)

# print(endpointOutputs)

parseAndSaveOutputFile(endpointOutputs, outputPath + currentFile + '.out')


# print(endpointVideoRanking)

