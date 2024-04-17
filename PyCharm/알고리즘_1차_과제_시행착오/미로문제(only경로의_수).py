PATHWAY = 0  # 길
WALL = 1     # 벽
VISITED = 2  # 방문 표시

# 입력 파트
N = int(input())

maze = []
for i in range(N):
    maze.append(list(map(int, input().split())))

K = int(input())

START = (0, 0)
GOAL = (N-1, N-1)

# 함수 파트
def solution(N, maze, start, goal, K):
    # 경로의 수
    path_counts = 0

    # 출발 좌표, 목표 좌표
    sx, sy = start
    gx, gy = goal

    # 유효 경로 탐색
    def pathfinder(x, y, path_length=0):
        nonlocal path_counts
        # 목적지에 도달하기 전 경로 길이가 목표를 초과한 경우 리턴
        if path_length > K: return

        # 목적지에 도달하면 카운트 증가
        if x == gx and y == gy:
            path_counts += 1
            return

        maze[y][x] = VISITED  # 방문 표시

        # 후보 좌표(이동할 수 있는 좌표)로 이동하여 탐색
        for a, b in selector(x, y):
            pathfinder(a, b, path_length + 1)  # 탐색 시 경로 길이 증가

        maze[y][x] = PATHWAY  # 방문 표시 초기화

    # 다음 후보 좌표 선정
    def selector(x, y):
        sel = []
        for dx, dy in list(zip([-1, 1, 0, 0], [0, 0, -1, 1])):
            (a, b) = (x + dx, y + dy)  # 후보 좌표 계산
            if N > a >= 0 and N > b >= 0 and maze[b][a] == PATHWAY:
                sel.append((x + dx, y + dy))
        return sel

    pathfinder(sx, sy)  # 탐색 실행

    return path_counts

# 출력 파트
print(solution(N, maze, START, GOAL, K))