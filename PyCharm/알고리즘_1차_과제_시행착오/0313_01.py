# N < 1000 개의 정수가 주어짐
# 또 하나의 정수 K가 주어짐
# 입력: (N, data, K)

# K의 rank는 N개의 정수 중 K보다 작은 것의 개수+1
# K의 rank를 판단하는 부분에서는 루프를 사용하면 안된다.
# 시간복잡도는 O(n)이하

# 입력
N = 10
data = [2, 5, 3, 8, 6, 7, 8, 7, 2, 1]
K = 8

def Rank(N, data, K):
    def check(i=0):
        if i == N:
            return 0
        else:
            return check(i+1) + (1 if data[i] < K else 0)

    return 1 + check()

# 출력
print(Rank(N, data, K))
