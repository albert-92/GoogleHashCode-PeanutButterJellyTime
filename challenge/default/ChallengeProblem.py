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

    def __init__(self, state, data):
        self.data = data
        self.cacheAssign = {c:[] for c in range(info['C'])}
        super(ChallengeProblem, self).__init__(state)

    def move(self):
        self.state = self.state

    def energy(self):
        return sum(self.state)

    def scoreAddVideo(self, cache, video):
        score = 0
        for endpointId in range(info['E']):
            for request in range(info['R']):
                if(requests[request]['Rv']==video):
                    minLatency, minLatCache = self.findBestLatency(video, endpointId)
                    newLatency = dict(endpoints[endpointId])[cache]
                    if(newLatency<minLatency):
                        score += -(newLatency-minLatency)
        return score




    def findBestLatency(self, video, endpointId):
        endpoint = endpoints[endpointId]
        connectedCaches = endpoint['K']
        minLatency =  endpoint['LD']
        minLatCache = -1
        for cache in range(connectedCaches):
            if video in self.cacheAssign[cache]:
                latency = dict(endpoint['Chaches'])[cache]
                if minLatency > latency:
                    minLatency = latency
                    minLatCache = cache
        return minLatency, minLatCache





# initial_state = []
# tsp = ChallengeProblem(initial_state)
# best_state, best_energy = tsp.anneal()

prob = ChallengeProblem(-1,-1)
print (prob.scoreAddVideo(0,0))