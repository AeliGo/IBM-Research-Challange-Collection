import json

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

    def __init__(self, dimension, dataset):
        self.dimension = dimension
        self.dataset = dataset

    def run(self):
        for data in self.dataset:
            self.generateRelationMap(str(data)).find3cycle().getCycles(
            ).generateProfile().getChunkedVertex()
            print(
                "-----------------------------------------------------------------------------------------------------------------------"
            )

    def getCycles(self):
        self.threeCycles = []
        for i in range(self.dimension):
            for cycle in self.threeCyclesMap[i]:
                self.checkIsNotExist(cycle) and self.threeCycles.append(cycle)
        return self

    def checkIsNotExist(self, cycle):
        for i in range(len(cycle)):
            cc = cycle + cycle
            if cc[i:i + len(cycle)] in self.threeCycles:
                return False
        return True

    def generateProfile(self):
        for i in range(self.dimension):
            self.profileMap[i] = {}
            for item in self.threeCyclesMap[i]:
                ss = item + item
                counts = []
                for edge in [ss[0:2], ss[1:3], ss[2:4]]:
                    counts.append(str(self.getEdgeInCycleCount(edge)))
                key = "".join(counts)
                self.profileMap[i][key] = self.profileMap[i][
                    key] + 1 if key in self.profileMap[i] else 1
                self.profileMap[i] = dict(sorted(self.profileMap[i].items()))
        return self

    def getChunkedVertex(self):
        self.chunkedVertex = []
        pointProfileDict = {}

        for key, value in self.profileMap.items():
            valueInJson = json.dumps(value)
            if valueInJson in pointProfileDict:
                pointProfileDict[valueInJson].append(key)
            else:
                pointProfileDict[valueInJson] = [key]
        self.chunkedVertex = list(pointProfileDict.values())
        return self

    def getEdgeInCycleCount(self, edge):
        count = 0
        for cycle in self.threeCycles:
            if edge[0] in cycle and edge[1] in cycle:
                count += 1
        return count

    def generateRelationMap(self, data):
        splitData = self.splitStr(self.dimension - 1, data, [])
        self.fillMap(splitData)
        return self

    def find3cycle(self):
        for i in range(self.dimension):
            self.threeCyclesMap[i] = []
            levelOne = self.relationMap[i]
            for ii in levelOne:
                levelTwo = self.relationMap[ii]
                for iii in levelTwo:
                    i in self.relationMap[iii] and self.threeCyclesMap[
                        i].append(str(i) + str(ii) + str(iii))
        return self

    # method used to split original data
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


dataset = [
    111100001110001101011101110111000000, 111100001011010110101001111011100101,
    111100001110010101101110110111100101, 111100001111000101011101110111100101,
    111100001110010011101010110111100101, 111100001010011110011011011110100010,
    111100001010011110101011101011001000, 111100001010101110011010111110001000,
    111100001010110110011101011111000101, 111100001010110110101100111111000101,
    111100001110100101011101110111000101, 111100001111000100111101110111000101,
    111100001010110110101010111011001000, 111100001010101110110010111011001000,
    111100001110001110011101111111000000
]

solution = solution(9, dataset)

# solution = solution(5, [1100101110])
solution.run()
