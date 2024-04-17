PATHWAY = 0  # 길
WALL = 1     # 벽
VISITED = 2  # 방문 표시

# 파일 입력 파트
with open('maze.txt', 'r') as file:
    file_content = file.read()

file_list = [list(map(int, line.split())) for line in file_content.split('\n')]

N, K = file_list[0][0], file_list[-1][0]
maze = file_list[1:-1]

START = (0, 0)
GOAL = (N-1, N-1)

# 함수 파트
def solution(N, maze, start, goal, K):
    # 휴식 횟수 리스트
    rest = []

    # 출발 좌표, 목표 좌표
    sx, sy = start
    gx, gy = goal

    # 유효 경로 탐색
    def pathfinder(x, y, direction='None', moves=0, counts=0):
        # 만일 일직선으로 이동할 수 있는 최대 길이인 경우, 길이를 초기화하고 휴식
        if moves >= K:
            moves = 0
            counts += 1

        # 목표 지점인 경우 휴식 횟수(count) 또는, 최대치만큼 일직선으로 이동하지 않은 경우 1을 더하여 추가한다.
        if x == gx and y == gy:
            rest.append(counts if moves == 0 else counts + 1)
            return

        maze[y][x] = VISITED  # 방문 표시

        # 후보 좌표(이동할 수 있는 좌표)로 이동하여 탐색
        # 이전에 이동한 방향과 다음으로 이동할 방향을 비교하여 일직선 이동 길이(moves)를 계승
        for a, b in selector(x, y):
            new_direction = director(x, y, a, b)
            if direction == new_direction:
                pathfinder(a, b, new_direction, moves + 1, counts)
            elif direction == 'None':
                pathfinder(a, b, new_direction, 1, counts)
            else:
                pathfinder(a, b, new_direction, 1, counts + 1)

        maze[y][x] = PATHWAY  # 방문 표시 초기화

    # 다음 후보 좌표 선정
    def selector(x, y):
        sel = []
        for dx, dy in list(zip([-1, 1, 0, 0], [0, 0, -1, 1])):
            (a, b) = (x + dx, y + dy)  # 후보 좌표 계산
            if N > a >= 0 and N > b >= 0 and maze[b][a] == PATHWAY:
                sel.append((x + dx, y + dy))
        return sel

    # 다음 이동 방향 판단(p: 현재 좌표, f:미래 좌표)
    def director(px, py, fx, fy):
        (dx, dy) = (fx - px, fy - py)  # 좌표 차이 계산
        directions = list(zip([-1, 1, 0, 0], [0, 0, -1, 1]))
        match = dict(list(zip(directions, ['A', 'D', 'W', 'S'])))

        return match[(dx, dy)]

    pathfinder(sx, sy)  # 탐색 실행

    return min(rest) if rest else -1  # 경로가 존재하면 최소 휴식 횟수, 아니면 -1을 반환한다.

# 출력 파트
print(solution(N, maze, START, GOAL, K))