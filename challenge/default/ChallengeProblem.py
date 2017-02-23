from simanneal import Annealer
from challenge.default.fileInput import *
from challenge.default.fileOutputv2 import *
from challenge.default.mainAlbertv3 import *
import math
import random

inputPath = '../input/'
outputPath = './outputv6/'

kittens = 'kittens'
me_at_the_zoo = 'me_at_the_zoo'
trending_today = 'trending_today'
videos_worth_spreading = 'videos_worth_spreading'

currentFile = me_at_the_zoo

info, videos, endpoints, requests = readAndParseInputFile(inputPath + currentFile + '.in')

# print(info)
# print(videos)
# print(endpoints)
# print(requests)


class ChallengeProblem(Annealer):

    def __init__(self, state):
        # state = {c:set() for c in range(info['C'])}
        super(ChallengeProblem, self).__init__(state)

    def move(self):
        for i in range(5):
            randomCache =  random.randint(0,info['C']-1)
            size = len(self.state[randomCache])
            randomVideo = random.randint(0, max(0,size-1))
            self.state[randomCache] = self.state[randomCache]

        for i in range(5):
            randomCache =  random.randint(0,info['C']-1)
            randomVideo = random.randint(0,info['V']-1)
            videoSizes = list(map(lambda x: videos[x], self.state[randomCache]))
            if((sum(videoSizes)+videos[randomVideo])<=info['X']):
                self.state[randomCache] = self.state[randomCache]|{randomVideo}

    def energy(self):
        return self.score()

    def score(self):
        score = 0
        for request in requests:
            numRequests = request['Rn']
            minLatency, minLatCache = self.findBestLatency(endpointId=request['Re'], videoId=request['Rv'])
            score += numRequests*minLatency
        return score



    def scoreAddVideo(self, cache, video):
        score = 0
        for endpointId in range(info['E']):
            for request in range(info['R']):
                if(requests[request]['Rv']==video):
                    minLatency, minLatCache = self.findBestLatency(video, endpointId)
                    newLatency = endpoints[endpointId][cache]
                    if(newLatency<minLatency):
                        score += -(newLatency-minLatency)
        return score


    def findBestLatency(self, endpointId, videoId):
        endpoint = endpoints[endpointId]
        connectedCaches = endpoint['K']
        minLatency =  endpoint['LD']
        minLatCacheId = -1
        for cacheId in range(connectedCaches):
            if videoId in self.state[cacheId]:
                connected, latency = self.getLatency(endpoint['Caches'], cacheId)
                if connected & (minLatency > latency):
                    minLatency = latency
                    minLatCacheId = cacheId
        return minLatency, minLatCacheId

    def getLatency(self, chaches, cacheId):
        for cache in chaches:
            if cache['c']==str(cacheId):
                return True, int(cache['Lc'])
        return False,0




# initial_state = []
# tsp = ChallengeProblem(initial_state)
# best_state, best_energy = tsp.anneal()

prob = ChallengeProblem(startState())
prob.updates = 10
prob.steps = 10000
best_state, best_energy = prob.anneal()
print(best_state)
print(best_energy)

parseAndSaveOutputFile(best_state, outputPath + currentFile + '.out')


