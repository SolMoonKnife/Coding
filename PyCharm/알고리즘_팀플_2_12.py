PATHWAY_COLOUR = "B"
WALL_COLOUR = "W"
BLOCKED_COLOUR = "X"
PATH_COLOUR = "P"

N = 3
maze = [
    ["B","B","B"],
    ["B","B","B"],
    ["B","B","B"]
]

def findMazePath(x, y):
    if (x < 0 or y < 0 or x >= N or y >= N or maze[x][y] != PATHWAY_COLOUR or maze[x][y] != PATH_COLOUR):
        return False
    elif (x == N-1 and y == N-1):
        maze[x][y] = PATH_COLOUR
        return True
    maze[x][y] = PATH_COLOUR
    if findMazePath(x-1, y) or findMazePath(x, y+1) or findMazePath(x+1, y) or findMazePath(x, y-1):
        return True
    maze[x][y] = BLOCKED_COLOUR
    return False

def countMazePath(x, y):
    path = 0
    if (x < 0 or y < 0 or x >= N or y >= N or maze[x][y] != PATHWAY_COLOUR):
        if (x == N-1 and y == N-1):
            maze[x][y] = PATH_COLOUR
            return 1
        return 0
    elif (x == N-1 and y == N-1):
        maze[x][y] = PATH_COLOUR
        return 1
    maze[x][y] = PATH_COLOUR
    directions = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]
    for d in directions:
        path += countMazePath(d[0], d[1])
    for i in maze:
        print(i)
    print()
    maze[x][y] = PATHWAY_COLOUR

    # if path == 0:
    #     maze[x][y] = BLOCKED_COLOUR

    return path



print(countMazePath(0, 0))
for i in maze:
    print(i)

