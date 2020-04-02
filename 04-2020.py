import numpy as np
from decimal import *

def Denary2Binary(num,digit):
  #returns the binary of integer n, using count number of digits
  return "".join([str((num >> y) & 1) for y in range(digit-1, -1, -1)])

def generateCombinationList(num):
  list = []
  #generate list of combinations
  for item in range(0, 2**num):
    list.append(Denary2Binary(item,num))
  return list

def initializeMatrix(dimention):
  return np.zeros((dimention,dimention))

def checkPointsConnected(indexs):
  if len(indexs) == 1:
    return True

  for i in indexs:
    copy = indexs.copy()
    copy.remove(i)
    record = []
    for j in copy:
      record.append(adjcentMatrix[i][j])
    if 1 not in record:
      return False
  return True

def checkDiffConnectWithBase(baseIndexs,index):
  baseList = np.array(adjcentMatrix)[:,baseIndexs]
  return True if baseList[index].sum() > 0 else False

# count how many connect line linked with base points
def getConnectedMap(baseIndexs,diffIndexs):
  if len(baseIndexs) == 0:
    raise Exception('base indexs cannot be empty')
  
  baseList = np.array(adjcentMatrix)[:,baseIndexs]

  if len(diffIndexs) == 0:
    return np.delete(baseList, baseIndexs, axis = 0)
  else:
    return baseList[diffIndexs]

# base and compare are string
# return [] or [index]
def checkIsProceedOrEqual(base,compare):
  indexs = []
  for count in range(len(base)):
    result = int(compare[count]) - int(base[count])
    if result < 0:
      return False
    elif result > 0:
      indexs.append(count)
  return indexs

def fillCoefficient(base,diffIndexs):
  allConnectdCount = getConnectedMap(base,[]).sum()
  # base dosen't change
  if len(diffIndexs) == 0:
    return (1 - possible) ** allConnectdCount

  # check if any diffIndexs connect with any of base indexs
  # each index must have at least one connect line with base indexs
  for diffIndex in diffIndexs:
    if checkDiffConnectWithBase(base,diffIndex) is False:
      return 0

  possibleMap = getConnectedMap(base,diffIndexs)
  otherConnectCount = allConnectdCount - possibleMap.sum()

  result = 1
  for item in possibleMap:
    result = result * (1 - (1 - possible) ** item.sum())

  return result * ((1 - possible) ** (otherConnectCount if otherConnectCount > 0 else 0))

def fillMatrix(emptyMatrix):
  for i in range(len(emptyMatrix)):
    for j in range(len(emptyMatrix[i])):
      row = Denary2Binary(i,5)
      col = Denary2Binary(j,5)

      # check and get diff indexs
      diff = checkIsProceedOrEqual(row,col)
      # base cannot be empty
      base = [index for index,ch in enumerate(row) if int(ch) == 1]
      if diff is not False and 0 in base and checkPointsConnected(base) is True:
        emptyMatrix[j][i] = fillCoefficient(base, diff)

  return  emptyMatrix

def transformState(matrix,state):
  matrix_one = np.array(matrix)
  matrix_two = np.array(state)
  return np.dot(matrix_one, matrix_two)

def calculateState(state,matrix,days):
  if days == 0:
    print(state)
    return state
  calculateState(transformState(matrix,state), matrix, days - 1)

adjcentMatrix = [[0,1,1,1,0],[1,0,0,0,1],[1,0,0,1,0],[1,0,1,0,1],[0,1,0,1,0]]
possible = Decimal("0.1")

combinationList = generateCombinationList(5)
matrix = fillMatrix(initializeMatrix(len(combinationList)))
state = []
for item in combinationList:
  if item == "10000":
    state.append(1)
  else:
    state.append(0)

calculateState(state,matrix,10)

