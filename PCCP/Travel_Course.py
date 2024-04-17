# 출발 공항 : "ICN" 고정
# 항공권 이차원 배열(tickets)은 출발지 공항과 도착지 공항 정보가 든 티켓 리스트를 가지고 있음
# ex) [["ICN", "JFK"], ["HND", "IAD"]]
# 모든 공항은 알파벳 3글자
# 주어지는 공항의 수는 3이상 10,000이하
# 티켓의 각 행은 0번 -> 1번 편도를 의미함
# 모든 티켓을 사용해야 함
# 가능한 경로가 2가지 이상인 경우 알파벳 순서가 앞서는 경로를 반환
# 모든 도시를 방문할 수 있는 경우만 주어짐

# def solution(tickets):
#
#     num = len(tickets)  # 항공권 개수 확인
#
#     # 예시 입력
#     # tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#
#     # 출발이 가능한 공항 : 0번에 존재하는 공항들
#     # 도착만 가능한 공항은 1번에 존재하는 공항 중 출발이 가능한 공항에 없는 공항
#     startable = []
#     for tkt in tickets:
#         if tkt[0] not in startable:
#             startable.append(tkt[0])
#     # ㄴ출발이 가능한 공항 리스트 생성
#     # 다음으로 출발이 가능한 공항에 대한 인접 리스트 생성
#     adj_list = [[] for _ in range(len(startable))]
#     for i in range(len(startable)):
#         # 출발 가능한 공항 수만큼 반복
#         for tkt in tickets:
#             # 모든 항공권에 대하여
#             if tkt[0] == startable[i] and tkt[1] not in adj_list[i]:
#                 adj_list[i].append(tkt[1])
#                 # 현재 확인중인 출발 가능 공항과 일치하는 항공권의
#                 # 도착 공항이 해당 출발 가능 공항의 인접 리스트에 없으면 추가
#
#     # 모든 공항에 대한 인접 리스트 생성 완료
#     adj_dict = dict(zip(startable, adj_list))
#     print(f'출발 가능 : {startable}')
#     print(adj_dict)
#
#     from collections import deque
#     Q = deque(["ICN"])
#     visited = []
#     while Q:
#         current = Q.popleft()
#         if current not in visited:
#             for destination in adj_dict[current]:
#             # 현재 공항에서 출발할 수 있는 목적지를 하나씩 추출
#             # 예를 들어 현재 공항이 HND 이면 IAD로 이동 가능, but IAD는 도착만 가능함
#             # 이런 경우는 현재 공항이 전체 경로의 뒤에서 두 번째여야 함
#             # 이 확인을 처음 Q에서 꺼냈을 때 판단해야 함
#                 if destination not in startable:
#                     # 목적지 리스트 중에 출발 불가능 공항이 있는 경우
#
#     return visited

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

def answer(tickets):
    routes = {}
    # 빈 딕셔너리
    # 티켓들을 하나씩 꺼냅니다 - 티켓의 원소는 리스트인데 출발, 도착 공항이죠
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
        # dictionary.get(key, default) <- 딕셔너리에서 해당 키를 갖는 값을 반환하며, 키가 없으면 기본값 반환
        # 위 문장은 출발지 키에 대하여 해당 키에 값(리스트)이 존재했으면 해당 리스트를 반환하여
        # 새로운 값(도착지)을 추가해 대입하는 것이고, 만일 해당 키가 딕셔너리에 없었던 경우
        # get함수는 빈 리스트를 기본값으로 반환하여 새로운 값을 리스트에 추가하고 값으로서 대입합니다.
    for r in routes:
        routes[r].sort(reverse=True)
        # 알파벳 순으로 정렬된 패스를 반환하라는 조건이 존재하므로 정렬을 수행해야 하는데
        # 리스트는 역순으로 꺼내는 것이 시간 복잡도 측면에서 이득이므로
        # 딕셔너리 내부의 각 리스트를 역순으로 정렬합니다.
    stack = ["ICN"]
    # 시작 공항은 고정되어 있으므로 ["ICN"] 스택 생성
    path = []
    # 빈 경로 생성
    while stack:
        top = stack[-1]
        # 스택의 탑을 확인함(꺼내지 않음)
        if top not in routes or len(routes[top]) == 0:
            # 꺼낸 공항이 딕셔너리(키)에 없거나 (=출발 공항이 아님), 해당 키에 대응하는 도착 공항이 0개라면
            path.append(stack.pop())
            # 스택에서 탑을 꺼내어 패스에 추가
        else:
            # 그렇지 않으면 (출발 공항이 존재하고, 또한 대응하는 도착 공항이 1개 이상인 경우)
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
            # 출발 공항에 대응하는 도착 공항 중 마지막 공항을 스택에 삽입
     # 마지막으로 완성된 패스를 역순으로 반환한다.
    # 패스에 추가하는 절차는 출발할 수 없는 공항(말단)을 만날 때만 이루어지고
    # 출발 가능 공항의 경우 다음 공항을 스택에 추가하며 해당 도착지를 제거하기 때문에
    # 패스는 역순으로 형성된다.
    return path[::-1]
# 정리하면 다음 공항이 존재하면 그 다음 공항을 스택에 넣고 해당 루트(항공권)을 사용한다.
# 즉 해당 출발지에 대한 도착지 정보를 삭제한다.
# 만일 스택에서 꺼낸 지점이 말단인 경우 최종적으로 패스에 추가된다.
# 스택이 모두 빌 때까지 해당 과정을 반복한다.

print(answer(tickets))
