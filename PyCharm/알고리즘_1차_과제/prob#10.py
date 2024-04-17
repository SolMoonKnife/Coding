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
        # 부피가 한도를 초과할 시 최저값 반환
        if volume > W:
            return float("-inf")
        
        # 최대 심도 도달 시 최종 가치에서 최종 폐기 비용을 뺀 값 반환
        if idx == N:
            return total_value - discard
        
        # 현재 아이템을 가져가는 것과, 폐기하는 것의 최종 가치를 계산
        valueIfIcd = dfs(idx+1, volume+data[idx][0], total_value+data[idx][1], discard)
        valueIfNot = dfs(idx+1, volume, total_value, discard+data[idx][2])
        
        # 둘 중 더 가치가 높은 쪽을 선택
        return max(valueIfIcd, valueIfNot)

    return dfs()

# 출력 파트
print(solution(data, N, W))

# best solution을 전역 변수처럼 실시간으로 관리하는 것도 좋아요

