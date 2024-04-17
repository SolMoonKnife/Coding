V, E = map(int, input().split())
adj_matrix = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end], adj_matrix[end][start] = 1, 1

from collections import deque
# 덱을 사용하여 리스트로 큐를 구현하는 것에 비해 시간복잡도에서 이점을 가짐
Q = deque([1])
visited = []

while Q:
    current = Q.popleft()  # dequeue와 같음

    if current not in visited:
        visited.append(current)

    for destination in range(V + 1):
        if adj_matrix[current][destination] and destination not in visited:
            visited.append(current)

print(visited)

