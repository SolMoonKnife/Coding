# 무방향 그래프, 인접 리스트
V, E = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)  # 쌍으로 연결

for i in adj_list:
    print(i)
