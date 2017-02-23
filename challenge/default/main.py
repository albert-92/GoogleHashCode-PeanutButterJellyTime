from challenge.default.fileInput import *
from challenge.default.fileOutput import *
import math

inputPath = '../input/'
outputPath = './output/'

kittens = 'kittens'
me_at_the_zoo = 'me_at_the_zoo'
trending_today = 'trending_today'
videos_worth_spreading = 'videos_worth_spreading'

currentFile = trending_today

info, videos, endpoints, requests = readAndParseInputFile(inputPath + currentFile + '.in')



# print(info)
# print(videos)
# print(endpoints)
# print(requests)