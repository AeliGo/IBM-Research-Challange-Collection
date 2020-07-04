def getFibonacciList(limit):
    result = []
    for n in range(limit):
        if n == 0:
            result.append(0)
        elif n == 1:
            result.append(1)
        else:
            result.append(result[n - 1] + result[n - 2])
    return result


def getGoldenRectangleNumber(n):
    if n < 1:
        print("Incorrect Golden Rectangle Number Input")
    
    return FibonacciList[n] * FibonacciList[n + 1]


def calculateTotalCount(initialMatrix):
    total = 0
    subMatrix = []
    for i in range(len(matrix_b)):
        subTotal = 0
        for j in range(len(matrix_b[0])):
            subTotal += matrix_b[i][j] * initialMatrix[j]
        subMatrix.append(subTotal)
        total += subTotal
    for k in range(len(subMatrix)):
        initialMatrix[k] = subMatrix[k]
    return total


def validation(limit):
    initialMatrix = [1, 0, 0, 0, 0]
    for count in range(limit):
        if count > 1:
            if calculateTotalCount(initialMatrix) != getGoldenRectangleNumber(
                    count):
                print("incorrect at ", count)
                break
            else:
                print("correct at ", count)

FibonacciList = getFibonacciList(10000)

matrix_a = [[1, 1, 1, 0], [1, 1, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0]]
matrix_b = [[0, 1, 2, 1, 0], [1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 0, 1, 1],
            [0, 0, 1, 1, 0]]

validation(9000)
