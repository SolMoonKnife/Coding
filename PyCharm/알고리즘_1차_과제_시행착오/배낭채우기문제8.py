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
    maximum_bag = 0

    def mkbag(contents=[], weight=0, price=0):
        nonlocal maximum_bag

        for item in range(N):
            next_weight = weight + w[item]
            if next_weight > W:
                if maximum_bag < price:
                    maximum_bag = price
                return
            next_price = price + v[item]
            if item not in contents:
                mkbag(contents+[item], next_weight, next_price)

    mkbag()

    return maximum_bag

# 출력 파트
import time
start = time.time()
print(solution(N, W, w, v))
end = time.time()

print("소요 시간:", f"{(end-start):.{32}f}")

