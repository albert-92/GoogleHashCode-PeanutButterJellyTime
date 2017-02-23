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

info, videos, endpoints, requests = readAndParseInputFile(inputPath + currentFile + '.in')

npArr = np.array([info, videos, endpoints, requests])

npArr.dump(inputPath + currentFile + '.dump')