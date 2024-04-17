# 파일 입력 파트
with open('input.txt', 'r') as file:
    file_content = file.read()

file_list = [list(map(int, line.split())) for line in file_content.split('\n')]

N = file_list[0][0]
W = file_list[1][0]
w = file_list[2]
v = file_list[3]

print(f'N: {N}, W: {W}\nw: {w}\nv: {v}')

# 함수 파트
def solution(N, W, w, v):
    bag = [[0 for _ in range(W+1)] for _ in range(N)]
    def bag_writer(item, weight):
        if item < 0 or weight == 0:
            return 0

        if bag[item][weight] != 0:
            return bag[item][weight]

        if weight < w[item]:
            result = bag_writer(item-1, weight)
        else:
            result = max(v[item] + bag_writer(item-1, weight-w[item]), bag_writer(item-1, weight))

        bag[item][weight] = result
        return result

    return bag_writer(N-1, W)

import time

start = time.time()
print(solution(N, W, w, v))
end = time.time()

print("소요 시간:", f"{(end-start):.{32}f}")