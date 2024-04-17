matrix = [
    [3,7,9],
    [4,2,6],
    [8,1,5]
]

# 3x3 행렬 (row, column)
(N, M) = (3, 3)

trails = []  # 행 우선 행렬 순회 리스트
new_trails = []

# 행 우선 순회
for r in range(N):
    for c in range(M):
        trails.append(matrix[r][c])

# 열 우선 순회 (0열-1열-2열 순으로 출력)
for c in range(M):
    for r in range(N):
        new_trails.append(matrix[r][c])

print(trails)
print(new_trails)


