'''

1. 답이 yes or no인 경우
pathfinder는 boolean값을 리턴한다.
내부적으로, 현재 좌표가 통로라면 가능한 모든 방향의 인접 셀에 pathfinder를 재귀 호출한다.
도중에 리턴되면 안되므로, 재귀 호출을 조건으로 하여 true인 경우에만 최종적으로 true를 리턴한다.
즉, 최종적으로 true가 리턴되는 경우는 어느 하나의 경로로 미로를 통과할 수 있음을 의미한다.

2.

'''

# 현재 위치 == 목표 위치: [현재 경로]를 [모든 경로]에 추가

# 도착이 아닌 경우: [이차원 방문 리스트]의 현재 좌표를 True로 표시
# 현재 위치에서 이동 가능한 모든 방향 탐색(후보 선출)
# 모든 후보에 대하여, 방문 리스트에 없다면 이동
#     현재 만들고 있는 경로에 다음 경로를 추가한다. (append)
#     다음 위치 재귀 호출
# [이차원 방문 리스트]의 현재 좌표를 False로 표시(다른 분기에서 방문할 수 있도록)

# 도착점에서 경로 +1 하는 것으로 경로 개수만 구하기로 수정 가능

PATHWAY = 0  # 길
WALL = 1     # 벽

origin_maze = """0 0 0 0 1 0 0 0
0 1 1 0 0 0 1 0
0 1 0 1 1 0 0 1
0 0 0 0 1 1 1 0
0 1 1 0 1 0 0 0
0 0 1 0 0 0 1 0
0 0 0 1 1 0 0 0
0 1 0 0 0 0 1 0"""

maze = [list(map(int, line.split())) for line in origin_maze.split("\n")]
for line in maze:
    print(line)

N = len(maze)

def maze_path(N, map):
    counts = 0
    whole_paths = []  # 찾은 모든 경로
    visited = [[False for _ in range(N)] for _ in range(N)]  # 방문 리스트
    tar = N-1  # 목표 좌표

    # 현재 위치 x, y를 기반으로 주변 경로를 재귀적으로 탐색한다.
    def pathfinder(x, y, path=[(0, 0)]):
        nonlocal counts
        # 현재 위치가 목표 위치라면, 현재 위치를 포함한 경로를 리스트에 추가한다.
        if x == tar and y == tar:
            return path

        # 현재 좌표에 방문 표시
        visited[y][x] = True

        # 다음 이동 위치 선정 (가능한 위치가 없는 경우: 막다른 길)
        candidates = selector(x, y)
        if candidates == []:
            return False

        for a, b in candidates:
            pro = pathfinder(a, b, path + [(a, b)])  # 다음 위치가 추가된 경로가 유효한가?
            # 막다른 길(False)이 아닌 경우, 찾은 경로를 추가
            if pro:
                whole_paths.append(pro)
                counts += 1

        # 다른 분기 탐색을 위하여 방문 표시 삭제
        visited[y][x] = False

    # 현재 위치 x, y를 기반으로 다음 이동할 위치 들을 선정한다.
    def selector(x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 좌 우 상 하
        selected = []
        for d in directions:
            if (x + d[0]) >= 0 and (y + d[1]) >= 0 and (x + d[0]) < N and (y + d[1]) < N and map[y + d[1]][x + d[0]] == PATHWAY and visited[y + d[1]][x + d[0]] == False:
                selected.append((x + d[0], y + d[1]))
        return selected
    
    # 탐색 시작
    pathfinder(0, 0)

    return whole_paths, counts

paths, counts = maze_path(N, maze)
for p in paths:
    print(p)

print("경로의 수:", len(paths))
print(counts)


# N-Queens
#
# function queens(현재 위치):
#     if 마지막 행:
#         True
#     elif 가능 위치:
#         가능한 모든 후보 위치에 대해 순환 호출
#     else:
#         False
#
# 대각선상 판정: 가로와 세로 차이가 같으면 동일 대각선상
#
# powerset(멱집합: 임의의 집합의 모든 부분 집합)
# -> 집합은 어떤 원소 하나를 포함하는 것과, 포함하지 않는 것 두 부류로 나눌 수 있음.
# 'a'가 포함된 집합에서 'a'를 제외한 나머지의 부분 집합을 모두 구하고, 그 부분 집합들에 다시 'a'를 추가한 집합을 추가한다.

# 알고리즘 문제는 멱집합 또는 순열을 생성하고(순환), 그것을 평가하는 구조에서 거의 벗어나지 않는다.