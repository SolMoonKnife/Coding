V, E = map(int, input().split())

# 인접 행렬이나 인접 리스트를 만든다.
adj_matrix  = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
adj_list    = [[] for _ in range(V + 1)]

# 무방향 그래프 간선 연결
for _ in range(E):
    start, end = map(int, input().split())
    # 인접 행렬에 추가
    adj_matrix[start][end], adj_matrix[end][start] = 1, 1
    
    # 인접 리스트에 추가
    adj_list[start].append(end)
    adj_list[end].append(start)

# DFS
stack = [1]
visited = []  # 방문했던 지점을 기록해야 함

while stack:
    # stack이 빌 때까지
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in range(V + 1):
        if adj_matrix[current][destination] and destination not in visited:
            stack.append(destination)
            # 현재 위치한 노드의 인접 노드 중 방문하지 않은 노드를 다음 방문할 스택에 추가
    
    # # 인접 행렬 대신 인접 리스트를 사용하는 방법
    # for destination in adj_list[current]:
    #     # 가능한 목적지를 현재 노드의 인접 리스트에서 추출
    #     if destination not in visited:
    #         stack.append(destination)
    #
    print(visited)

# DFS 재귀 해법 - 1000회 이상 연산되면 에러를 발생하므로 사용하지 않는 것이 좋음
# def dfs(n):
#     if n not in visited:
#         visited.append(n)
#     for destination in range(V + 1):
#         if adj_matrix[n][destination] and destination not in visited:
#             dfs(destination)
#
# visited = []
# dfs(1)
#
# print(visited)