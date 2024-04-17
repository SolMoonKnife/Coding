# depart: start/ transit: tmp/ arrival: end
def towerOfHanoi(N, depart, transit, arrival):
    def diskMove(N, depart, transit, arrival):
        if N == 1:
            pathStack.append((depart, arrival, N))
        elif N > 1:
            diskMove(N-1, depart, arrival, transit)
            pathStack.append((depart, arrival, N))
            diskMove(N-1, transit, depart, arrival)

    pathStack = []
    diskMove(N, depart, transit, arrival)

    return pathStack

def printHanoiPath(path):
    for s, e, d in path:
        print(f"Disk[{d}]: [{s}] → [{e}]")
    print(f"Total movements: {len(path)}, End")

N = 5
path = towerOfHanoi(N, 'A', 'B', 'C')
printHanoiPath(path)