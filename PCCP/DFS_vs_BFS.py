graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H'],
    'F': ['C', 'I'],
    'G': ['D'],
    'H': ['E'],
    'I': ['F', 'J'],
    'J': ['I']
}
from collections import deque
def bfs(graph, start_node):
    Q = deque([start_node])
    visited = []
    while Q:
        current = Q.popleft()
        if current not in visited:
            visited.append(current)

        for destination in graph[current]:
            if destination not in visited:
                visited.append(destination)  # bfs는 같은 깊이의 모든 노드를 즉시 방문하므로 여기서도 추가
                Q.append(destination)

    return visited
print(f'bfs : {bfs(graph, 'A')}')

def dfs(graph, start_node):
    Stk = ['A']
    visited = []
    while Stk:
        current = Stk.pop()
        if current not in visited:
            visited.append(current)

        for destination in graph[current]:
            if destination not in visited:
                Stk.append(destination)  # dfs는 방문할 노드를 스택에 넣기만 하고 차례대로 최대 깊이까지 방문하므로 여기서 추가x

    return visited

print(f'dfs : {dfs(graph, 'A')}')
