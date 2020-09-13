import json
from itertools import permutations

from dataset import dataset9, dataset11, dataset12

# reference:
# http://uplsj.com/wp-content/uploads/2020/09/rps.pdf


class solution:
    dimension = 0
    dataset = []

    relationMap = {}
    threeCycles = []
    threeCyclesMap = {}
    profileMap = {}
    chunkedVertex = []
    am = []

    def __init__(self, dimension, dataset):
        self.dimension = dimension
        self.dataset = dataset

    def run(self):
        for data in self.dataset:
            #clear am container
            self.am = []

            self.generateRelationMap(str(data))
            self.generateCycleMap()
            self.getCycles()
            self.generateProfile()
            self.getChunkedVertices()
            self.searchAutomorphism(self.chunkedVertex, 0,
                                    [i for i in range(self.dimension)])
            if len(self.am) > 1:
                print("Total Ams:", len(self.am))
                print("Solution:", self.relationMap)
                print("----------------------------------------------------")

    def generateRelationMap(self, data):
        splitData = self.splitStr(self.dimension - 1, data, [])
        self.fillMap(splitData)

    # method to split original data
    # "111100001110001101011101110111000000"  => ['11110000', '1110001', '101011', '10111', '0111', '000', '00', '0']
    def splitStr(self, D, originalStr, container=[]):
        if D == 0:
            return container
        else:
            container.append(originalStr[0:D])
            return self.splitStr(D - 1, originalStr[D:], container)

    # fill relationMap by given original data
    def fillMap(self, splitArr):
        for i in range(self.dimension):
            self.relationMap[i] = []
        for x, item in enumerate(splitArr):
            for i, value in enumerate(item):
                y = i + x + 1
                if int(value) == 1:
                    self.relationMap[x].append(y)
                else:
                    self.relationMap[y].append(x)

    def generateCycleMap(self):
        for i in range(self.dimension):
            self.threeCyclesMap[i] = []
            levelOne = self.relationMap[i]
            for ii in levelOne:
                levelTwo = self.relationMap[ii]
                for iii in levelTwo:
                    i in self.relationMap[iii] and self.threeCyclesMap[
                        i].append(str(i) + str(ii) + str(iii))

    def getCycles(self):
        self.threeCycles = []
        for i in range(self.dimension):
            for cycle in self.threeCyclesMap[i]:
                self.checkIsNotExist(cycle) and self.threeCycles.append(cycle)

    def checkIsNotExist(self, cycle):
        for i in range(len(cycle)):
            cc = cycle + cycle
            if cc[i:i + len(cycle)] in self.threeCycles:
                return False
        return True

    # check is automorphism
    def checkIsAm(self, permutationIndices):
        for i in range(self.dimension):
            for j in range(self.dimension):
                original = 0 if j in self.relationMap[i] else 1
                current = 0 if permutationIndices[j] in self.relationMap[
                    permutationIndices[i]] else 1
                if original != current:
                    return False
        return True

    def generateProfile(self):
        for i in range(self.dimension):
            self.profileMap[i] = {}
            for item in self.threeCyclesMap[i]:
                ss = item + item
                counts = []
                for edge in [ss[0:2], ss[1:3], ss[2:4]]:
                    counts.append(self.getEdgeInCycleCount(edge))
                counts.sort()
                key = "".join([str(count) for count in counts])
                self.profileMap[i][key] = self.profileMap[i][
                    key] + 1 if key in self.profileMap[i] else 1
                self.profileMap[i] = dict(sorted(self.profileMap[i].items()))

    def getEdgeInCycleCount(self, edge):
        count = 0
        for cycle in self.threeCycles:
            if edge[0] in cycle and edge[1] in cycle:
                count += 1
        return count

    def getChunkedVertices(self):
        self.chunkedVertex = []
        pointProfileDict = {}
        for key, value in self.profileMap.items():
            valueInJson = json.dumps(value)
            if valueInJson in pointProfileDict:
                pointProfileDict[valueInJson].append(key)
            else:
                pointProfileDict[valueInJson] = [key]
        self.chunkedVertex = list(pointProfileDict.values())

    def searchAutomorphism(self, chunkedVertex, index, permutationIndices):
        if index >= len(chunkedVertex):
            if self.checkIsAm(permutationIndices) == True:
                self.am.append(permutationIndices)
                # print("AM: ", permutationIndices)
        else:
            chunk = chunkedVertex[index]
            purmuList = list(permutations(chunk))
            for perm in purmuList:
                for i, p in enumerate(chunk):
                    permutationIndices[p] = perm[i]
                self.searchAutomorphism(chunkedVertex, index + 1,
                                        [p for p in permutationIndices])


# solution9 = solution(9, dataset9)
solution11 = solution(11, dataset11)
# solution9.run()
solution11.run()
