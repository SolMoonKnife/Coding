def dfs(data, idx, weight, total_value, remaining_discard, max_weight):
    if weight > max_weight:  # 무게 제한을 초과하면 종료
        return float('-inf')

    if idx == len(data):  # 모든 아이템을 고려했을 때 종료
        return total_value - remaining_discard

    # 현재 아이템을 선택하는 경우
    select_current = dfs(data, idx + 1, weight + data[idx][0], total_value + data[idx][1], remaining_discard,
                         max_weight)

    # 현재 아이템을 선택하지 않는 경우
    discard_current = dfs(data, idx + 1, weight, total_value, remaining_discard + data[idx][2], max_weight)

    # 두 경우 중 더 큰 값을 선택
    return max(select_current, discard_current)


def maximize_final_value(N, data, W):
    return dfs(data, 0, 0, 0, 0, W)


# 입력 파트
with open("input10.txt", "r") as file:
    file_contents = file.read()

file_list = [list(map(int, line.split())) for line in file_contents.split('\n')]

for line in file_list:
    print(line)

N = file_list[0][0]
data = file_list[1:-1]
W = file_list[-1][0]

# 최대 최종 가치 계산
max_final_value = maximize_final_value(N, data, W)
print("최대 최종 가치:", max_final_value)
