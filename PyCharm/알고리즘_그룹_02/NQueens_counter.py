cols = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
N = 4

def promising(level):
    return True

def queens(level) -> int:
    if not promising(level):
        return 0
    elif level == N:
        return 1

    for i in range(1, N):
        cols[level+1] = i
