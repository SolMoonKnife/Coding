# 입력 파트
with open("input10.txt", "r") as file:
    file_contents = file.read()

file_list = [list(map(int, line.split())) for line in file_contents.split('\n')]

N = file_list[0][0]
data = file_list[1:-1]
W = file_list[-1][0]

# 함수 파트
def solution(data, N, W):

    def dfs(idx=0, volume=0, total_value=0, discard=0):
        if volume > W:
            return float("-inf")

        if idx == N:
            return total_value - discard

        valueIfIcd = dfs(idx+1, volume+data[idx][0], total_value+data[idx][1], discard)
        valueIfNot = dfs(idx+1, volume, total_value, discard+data[idx][2])

        return max(valueIfIcd, valueIfNot)

    return dfs()

print(solution(data, N, W))

