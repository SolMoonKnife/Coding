'''
아래 그림과 같이 폭탄(2)이 설치된 미로가 있다.
폭탄이 설치된 곳을 지나갈 수는 있지만 대신 부상을 당하는데,
K번을 초과하여 부상을 당하면 죽는다.

출구까지 죽지 않고 갈 수 있는지 검사하여
Yes 혹은 No를 출력하는 프로그램을
순환함수(recursion)를 이용하여 작성하라.
'''
# 상수 정의
PATHWAY = 0
WALL    = 1
BOMB    = 2
VISITED = -1

# 입력 파트
N = int(input())

maze = []
for _ in range(N):
    maze.append(list(map(int, input().split())))

K = int(input())

# 에코 출력
# print(f'N: {N}, K: {K}')
# for i in range(N):
#     print(maze[i])

START = (0, 0)
GOAL = (N-1, N-1)

# solution(미로 크기, 미로, 출발점, 도착점, 폭발 한도)
def solution(N, maze, start, goal, K):
    (sx, sy), (gx, gy) = start, goal
    
    # pathfinder(현재 x좌표, 현재 y좌표, 피격 횟수)
    def pathfinder(x, y, hits=0, depth=0):
        # 에코 출력
        # indentation = "  " * depth
        # print(f"{indentation}Depth[{depth}], 탐색 위치: ({x}, {y}, [{maze[y][x]}]), 부상: {hits})")

        # 부상 횟수 확인, 초과 시 False반환
        if hits > K:
            return False

        # 목적지 도착 여부 확인, 도착 시 True반환
        if x == gx and y == gy:
            return True

        maze[y][x] = VISITED  # 방문 표시

        # 재귀적 탐색
        for nx, ny in selector(x, y):
            result = pathfinder(nx, ny, (hits + 1)if maze[ny][nx] == BOMB else hits, depth+1)
            if result:
                return True

        maze[y][x] = PATHWAY  # 방문 표시 해제

    # 다음 후보 좌표 선정
    def selector(x, y):
        sel = []
        for dx, dy in list(zip([-1, 1, 0, 0], [0, 0, -1, 1])):
            (a, b) = (x + dx, y + dy)  # 후보 좌표 계산
            if N > a >= 0 and N > b >= 0 and (maze[b][a] == PATHWAY or maze[b][a] == BOMB):
                sel.append((x + dx, y + dy))
        return sel

    return "Yes" if pathfinder(sx, sy) else "No"

print(solution(N, maze, START, GOAL, K))