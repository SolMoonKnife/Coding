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
    for item in range(N):
        for weight in range(W+1):
            if w[item] > weight:
                bag[item][weight] = bag[item-1][weight]
            else:
                bag[item][weight] = max(v[item] + bag[item-1][weight - w[item]], bag[item-1][weight])

    return bag[N-1][W]

print(solution(N, W, w, v))