# with open("input9.txt", "r") as file:
#     file_contents = file.read()
#
# file_list = [list(map(int, line.split())) for line in file_contents.split('\n')]
#
# N = file_list[0][0]
# data = file_list[1:N+1]
# k = file_list[N+1][0]

MAX_STATUS = 999999
def solution(N, data, k):
    # 탐욕 기법 시도
    favor = [[[None, None] for _ in range(N)] for _ in range(N)]  # 선호도를 저장하는 N*N 행렬

    for i in range(N):
        for j, v in enumerate(data[i]):
            if i != j:
                favor[i][j] = [j, v]
            else:
                favor[i][j] = [None, -MAX_STATUS -1]
        favor[i].sort(key=lambda x: x[1], reverse=True)
    
    # 특정 팀에 속한 개인 i의 종합 능력치를 계산하는 익명 함수
    stat = lambda i, team: data[i][i] + sum(e for idx, e in enumerate(data[i]) if (idx != i) and idx in team)

    status = [0 for _ in range(N)]
    for i in range(N):
        # 모든 개인 i에 대해 선호도가 높은 순서로 팀을 구성
        team = [i]
        teammates = favor[i][:k-1]
        for e in teammates:
            team += [e[0]]

        # 구성된 팀에 대해 각 개인의 종합 능력치를 합산
        for t in team:
            status[i] += stat(t, team)

    return max(status)

import numpy as np
import time

def mkhuman(N):
    humans = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            humans[i][j] = int(100*np.random.rand()-50)
    return humans
N = 10000
data = mkhuman(N)

start = time.time()
print(solution(N, data, 20))
end = time.time()

print(f"소요 시간:{end-start:.{48}f}")