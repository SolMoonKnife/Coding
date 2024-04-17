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
