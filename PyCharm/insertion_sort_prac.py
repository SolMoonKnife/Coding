# 삽입 정렬을 구현하세요.
# 이중 join 함수 레전드;;
import time
from numpy import random as R
def solution(data):
    for i in range(len(data)):
        target = data[i]

        k = 0
        while data[k] < target and k < i:
            k += 1

        if k != i:
            for j in range(i-1, k-1, -1):
                data[j+1] = data[j]
            data[k] = target

    return data

data = [int(1000 * R.rand()) for _ in range(1000)]

showwer = lambda d: "\n".join(", ".join(map(str, (e for e in d[i:i+20]))) for i in range(0, len(d), 20))

print('[original]')
print(showwer(data))

s = time.time()
solved = solution(data)
e = time.time()

print('\n[solved]')
print(showwer(data))

print('remaining:', f"{(e - s):.{12}f}")

# 외울 것
# 소수점 표기법 <- f문자열 활용
tmp = 1.23456789098765432
print(f"{tmp:.{5}f}")
print(f"{tmp:.{10}f}")
print(f"{tmp:.{15}f}")
