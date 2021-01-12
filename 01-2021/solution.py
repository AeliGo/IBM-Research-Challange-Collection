def initializeMap(positions, length):
    result = [0] * length
    for i in positions:
        result[i] = None
    return result


def checkFullyVaccinated(grid):
    for cell in grid:
        if cell == 0 or cell == 1:
            return False
    return True


# motion = 1 , clockwise
# motion = -1, counterclockwise
def changeDirection(direction, motion=1):
    directions = ["up", "right", "down", "left"]
    index = directions.index(direction)
    if motion > 0:
        return directions[0] if index == 3 else directions[index + 1]
    if motion < 0:
        return directions[3] if index == 0 else directions[index - 1]


def getTargetIndex(index, direction):
    dimensionSquare = dimension * dimension
    if direction == "up":
        return index + dimensionSquare - dimension if index - dimension < 0 else index - dimension
    if direction == "down":
        return index + dimension if index + dimension < dimensionSquare else index + dimension - dimensionSquare
    if direction == "left":
        return index - 1 + dimension if index % dimension == 0 else index - 1
    if direction == "right":
        return index + 1 - dimension if (index +
                                         1) % dimension == 0 else index + 1


def botGoOnAdventure(currentIndex, targetDirection, grid):
    index = currentIndex
    direction = targetDirection
    count = 0

    while count <= 4 * dimension:
        value = grid[index]
        if value == None:
            #turns 90 degrees counterclockwise
            direction = changeDirection(direction, -1)
            count += 1
        if value == 0:
            #administers one dose
            grid[index] = 1
            #turns 90 degrees clockwise
            direction = changeDirection(direction, 1)
            count = 0
        if value == 1:
            #administers one dose
            grid[index] = 2
            #turns 90 degrees counterclockwise
            direction = changeDirection(direction, -1)
            count = 0
        if value == 2:
            count += 1
        #takes one step forward
        index = getTargetIndex(index, direction)

    return checkFullyVaccinated(grid)


def getCoordinate(index, dimension):
    x = index // dimension
    y = index % dimension
    return (x, y)


def findSolution(dimension):
    dimensionSquare = dimension * dimension
    for i in range(dimensionSquare):
        for j in range(i + 1, dimensionSquare):
            grid = initializeMap([i, j], dimensionSquare)
            if botGoOnAdventure(0, "up", grid) == True:
                print(
                    "Position Found:",
                    [getCoordinate(i, dimension),
                     getCoordinate(j, dimension)])
                return


dimension = 50
findSolution(dimension)
