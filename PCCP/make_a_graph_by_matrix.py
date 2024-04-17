# 무방향 그래프, 인접 행렬
V, E = list(map(int,input().split()))

adj_matrix = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end], adj_matrix[end][start] = 1, 1

for i in adj_matrix:
    print(i)
