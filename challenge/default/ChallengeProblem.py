from simanneal import Annealer
from challenge.default.fileInput import *
from challenge.default.fileOutput import *
import math

inputPath = '../input/'
outputPath = './output/'

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
        self.state = {c:[] for c in range(info['C'])}
        super(ChallengeProblem, self).__init__(state)

    def move(self):
        self.state = self.state

    def energy(self):
        return sum(self.state)

    def score(self):
        score = 0
        for request in requests:
            numRequests = request['Rn']
            minLatency, minLatCache = self.findBestLatency(endpointId=request['Re'], videoId=request['Rv'])
            score += numRequests*minLatency



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
        minLatCache = -1
        for cacheId in range(connectedCaches):
            if videoId in self.state[cacheId]:
                connected, latency = self.getLatency(endpoint['Chaches'], cacheId)
                if connected & minLatency > latency:
                    minLatency = latency
                    minLatCacheId = cacheId
        return minLatency, minLatCacheId

    def getLatency(self, chaches, cacheId):
        for cache in chaches:
            if cache['c']==cacheId:
                return True, cache['Lc']
        return False,0




# initial_state = []
# tsp = ChallengeProblem(initial_state)
# best_state, best_energy = tsp.anneal()

prob = ChallengeProblem(-1)
