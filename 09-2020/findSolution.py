import numpy as np

class solution:
    dimension = 0
    dataset = []

    relationMap = {}
    threeCyclesMap = {}
    allPossibleAutomorphism = []
    automorphism = []

    def __init__(self, dimension, dataset):
        self.dimension = dimension
        self.dataset = dataset

    def run(self):
        for data in dataset:
            self.generateRelationMap(str(data)).find3cycle(
            ).getPossibleAutomorphism().filterAutomorphism()

    def getPossibleAutomorphism(self):
        for i in range(self.dimension):
            self.concatCycle(i, "")
        return self

    def concatCycle(self, i, container):
        if len(container) == self.dimension and self.isUnique(container):
            self.allPossibleAutomorphism.append(container)
        else:
            for item in self.threeCyclesMap[i]:
                text = container[0:-1] + item
                if self.isUnique(text):
                    self.concatCycle(int(item[-1]), text)
                    if len(container) > 0:
                        self.allPossibleAutomorphism.append(container)

    def isUnique(self, str):
        n = len(str)
        i = 0
        while i != n:
            if str[i] in str[i + 1:]:
                return False
            i += 1
        return True

    def filterAutomorphism(self):
        for automorphism in self.allPossibleAutomorphism:
            if self.checkIsAutomorphism(automorphism):
                self.automorphism.append(automorphism)
        print(self.automorphism)
        return self

    def checkIsAutomorphism(self, automorphism):
        for i in range(self.dimension):
            for item in self.threeCyclesMap[i]:
                isTrue = False
                ss = item + item
                aa = automorphism + automorphism
                for textThree in [ss[0:3], ss[1:4], ss[2:5]]:
                    if textThree in aa:
                        isTrue = True
                if isTrue == False:
                    return False
                    # for textTwo in [[ss[0:2], ss[2:3]], [ss[1:3], ss[3:4]],
                    #                 [ss[2:4], ss[4:5]]]:
                    #     if textTwo[0] in aa and textTwo[1] in aa:
                    #         return False
        return True

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
                    if i in self.relationMap[iii]:
                        self.threeCyclesMap[i].append(
                            str(i) + str(ii) + str(iii))
        print(self.threeCyclesMap)
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
        y = 0
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
