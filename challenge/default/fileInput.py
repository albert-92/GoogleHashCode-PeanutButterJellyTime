def readAndParseInputFile(inputFilePath):

    with open(inputFilePath) as f:
        lines = [line.rstrip('\n') for line in f]

    firstLineSplittet = lines.pop(0).split()

    info = {
        'V': int(firstLineSplittet[0]),
        'E': int(firstLineSplittet[1]),
        'R': int(firstLineSplittet[2]),
        'C': int(firstLineSplittet[3]),
        'X': int(firstLineSplittet[4])
    }

    nextLineSplittet = lines.pop(0).split()

    # print(info)

    videos = []

    for video in nextLineSplittet:
        videos.append(int(video))

    # print(videos)

    endpoints = []

    for e in range(info['E']):


        nextLineSplittet = lines.pop(0).split()

        endpoint = {
            'LD': int(nextLineSplittet[0]),
            'K': int(nextLineSplittet[1]),
            'Caches': []
        }

        # print(endpoint['K'])

        for k in range(endpoint['K']):

            nextLineSplittet = lines.pop(0).split()

            endpoint['Caches'].append(
                {
                    'c': nextLineSplittet[0],
                    'Lc': nextLineSplittet[1]
                }
            )

        endpoints.append(endpoint)

    # print(endpoints)

    requests = []

    for line in lines:
        nextLineSplittet = line.split()

        request = {
            'Rv': int(nextLineSplittet[0]),
            'Re': int(nextLineSplittet[1]),
            'Rn': int(nextLineSplittet[2])
        }

        requests.append(request)

    # print(requests)

    return info, videos, endpoints, requests


