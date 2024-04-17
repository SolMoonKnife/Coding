mapping = lambda text: list(map(int, text.split(' ')))
# 입력
N = 25
data = mapping("1 3 6 9 13 17 21 23 24 31 37 38 44 45 47 51 55 58 71 73 88 91 99 101 102")
K = 72

def Nearest(N, data, K):
    transPos = lambda x: x if x >= 0 else -x

    def compare(i=0, smallest=999999, diff=999999):
        if i == N:
            return smallest
        else:
            judge = transPos(data[i] - K) >= diff
            return compare(i+1, smallest if judge else data[i], diff if judge else transPos(data[i] - K))

    return compare()

# 출력
print(Nearest(N, data, K))
