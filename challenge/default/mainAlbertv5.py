from challenge.default.fileInput import *
from challenge.default.fileOutput import *
import math

import numpy as np

import operator

inputPath = '../input/'
outputPath = './outputv5/'

kittens = 'kittens'
me_at_the_zoo = 'me_at_the_zoo'
trending_today = 'trending_today'
videos_worth_spreading = 'videos_worth_spreading'

currentFile = trending_today

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

endpointVideoRanking = []

# endpointVideoRanking = np.array(endpointVideoRanking)



# print(endpointVideoRanking)

# endpointVideoRankingTemp = np.copy(endpointVideoRanking)

possibleCaches = []

sortedRequests = sorted(requests, key=operator.itemgetter('Rn'), reverse=True)




for c in range(info['C']):
    possibleCaches.append({'videos':[], 'size': 0})


print(len(sortedRequests))
for c in range(info['C']):
    print(c, info['C'])

    if (possibleCaches[c]['size'] < info['X']):
        for request in sortedRequests:
            endpoint = endpoints[request['Re']]
            sortedCaches = sorted(endpoint['Caches'], key=operator.itemgetter('Lc'))

            if (len(sortedCaches) > c):

                bestCache = possibleCaches[sortedCaches[c]['c']]

                video = videos[request['Rv']]

                if bestCache['size'] + videos[request['Rv']] <= info['X'] and not (request['Rv'] in bestCache['videos']):
                    bestCache['videos'].append(request['Rv'])
                    bestCache['size'] += videos[request['Rv']]
                    sortedRequests.remove(request)

print(len(sortedRequests))


# for e in range(info['E']):
#     endpointVideoRanking[str(e)] = sorted(endpointVideoRanking[str(e)].items(), key=operator.itemgetter(1),
#     reverse=True)
#
# for cacheNum in range(info['C']):
#     print(cacheNum, info['C'])
#     for e in range(info['E']):
#
#         # print(endpointVideoRanking[str(e)])
#
#         # find best cache
#
#         # sortedCaches = newlist = sorted(endpoints[e]['Caches'], key=lambda k: k['Lc'])
#         sortedCaches = sorted(endpoints[e]['Caches'], key=operator.itemgetter('Lc'))
#
#         if (len(sortedCaches) > cacheNum):
#
#             bestCache = possibleCaches[sortedCaches[cacheNum]['c']]
#
#             for video in endpointVideoRanking[str(e)]:
#                 if bestCache['size'] + videos[int(video[0])] <= info['X'] and not (video[0] in bestCache['videos']):
#                     bestCache['videos'].append(video[0])
#                     endpointVideoRanking[str(e)].remove(video)
#                     bestCache['size'] += videos[int(video[0])]


# chachesOutput = list(np.array(possibleCaches)[:info['C']])

outputCaches = []

for c in possibleCaches:
    outputCaches.append(c['videos'])

parseAndSaveOutputFile(outputCaches, outputPath + currentFile + '.out')


# print(endpointVideoRanking)

