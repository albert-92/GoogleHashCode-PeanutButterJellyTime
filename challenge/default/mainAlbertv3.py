from challenge.default.fileInput import *
from challenge.default.fileOutput import *
import math

import numpy as np

import operator

def startState():

    inputPath = '../input/'
    outputPath = './output/'

    kittens = 'kittens'
    me_at_the_zoo = 'me_at_the_zoo'
    trending_today = 'trending_today'
    videos_worth_spreading = 'videos_worth_spreading'

    currentFile = me_at_the_zoo

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

    for c in range(info['C']):
        possibleCaches.append({'videos':[], 'size': 0})

    for e in range(info['E']):
        endpointVideoRanking[str(e)] = sorted(endpointVideoRanking[str(e)].items(), key=operator.itemgetter(1),
        reverse=True)

    for cacheNum in range(info['C']):
        print(cacheNum, info['C'])
        for e in range(info['E']):

            # print(endpointVideoRanking[str(e)])

            # find best cache

            # sortedCaches = newlist = sorted(endpoints[e]['Caches'], key=lambda k: k['Lc'])
            sortedCaches = sorted(endpoints[e]['Caches'], key=operator.itemgetter('Lc'))

            if (len(sortedCaches) > cacheNum):

                bestCache = possibleCaches[sortedCaches[cacheNum]['c']]

                for video in endpointVideoRanking[str(e)]:
                    if bestCache['size'] + videos[int(video[0])] <= info['X'] and not (video[0] in bestCache['videos']):
                        bestCache['videos'].append(video[0])
                        bestCache['size'] += videos[int(video[0])]


    # chachesOutput = list(np.array(possibleCaches)[:info['C']])

    outputCaches = {}

    i = 0

    for c in possibleCaches:
        newSet = set()

        for video in c['videos']:
            newSet.add(int(video))

        outputCaches[i] = newSet

        i += 1

    # parseAndSaveOutputFile(outputCaches, outputPath + currentFile + '.out')

    # print(outputCaches)

    return outputCaches

    # CP = ChallengeProblem(outputCaches)
    # print(endpointVideoRanking)

