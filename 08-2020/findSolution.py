def getAllNodes():
    nodes = []
    for z in range(101):
        for y in range(z + 1):
            for x in range(y + 1):
                nodes.append((x, y, z))
    nodes.sort(key=sum)
    return nodes


def generateStatusCollection(nodes):
    winRules = []
    loseRules = [(0, 0, 0)]

    statusMap = []
    for node in nodes:
        if node in loseRules:
            statusMap.append("L")
        elif node in winRules:
            statusMap.append("W")
        else:
            statusMap.append("U")
    return statusMap


def getPositionCollection(nodes):
    #get node map with value as key, index as value
    nodesMap = {}
    for index, node in enumerate(nodes):
        nodesMap[node] = index

    calculateSets = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1),
                     (0, 1, 1), (1, 1, 1)]
    collection = []
    for node in nodes:
        targetPosition = []
        originPosition = list(node)
        for cSet in calculateSets:
            step = 1
            while True:
                a = originPosition[0] + cSet[0] * step
                b = originPosition[1] + cSet[1] * step
                c = originPosition[2] + cSet[2] * step
                if a > 100 or b > 100 or c > 100:
                    break
                targetPosition.append(nodesMap[tuple(sorted([a, b, c]))])
                step += 1
        positions = list(set(targetPosition))
        collection.append(positions)
    return collection


def findSolution():
    nodes = getAllNodes()
    statusCollection = generateStatusCollection(nodes)
    positionCollection = getPositionCollection(nodes)

    for idx, status in enumerate(statusCollection):
        if status == "L":
            for p in positionCollection[idx]:
                if statusCollection[p] == "U":
                    statusCollection[p] = "W"
        if status == "U":
            statusCollection[idx] = "L"
    



findSolution()