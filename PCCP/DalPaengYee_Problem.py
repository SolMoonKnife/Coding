dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]  # 우하좌상

n = int(input('N : '))

matrix = [[0 for _ in range(n)] for _ in range(n)]  # 이차원 리스트 만들기 외워라

x, y = 0, 0  # 시작 좌표
num = 1  # 기록할 숫자
dir = 0  # 이동 방향(우하좌상) 지시
while True:
    matrix[x][y] = num
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0:
        x, y = nx, ny
    else:
        dir = (dir + 1) % 4  # 1, 2, 3, 4->0
        x += dx[dir]
        y += dy[dir]
    num += 1
    if num > (n * n):
        break

for row in matrix:
    for column in range(len(row)):
        if column != len(row) - 1:
            print(row[column], end=' ')
        else:
            print(row[column])