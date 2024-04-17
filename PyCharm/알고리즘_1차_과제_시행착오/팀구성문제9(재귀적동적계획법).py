# 입력 파트
with open("input9.txt", "r") as file:
    file_contents = file.read()

file_list = [list(map(int, line.split())) for line in file_contents.split('\n')]

N = file_list[0][0]
data = file_list[1:N+1]
k = file_list[N+1][0]

# 함수 파트
def solution(data, N, k):
    # 상태 최적해를 저장할 딕셔너리 (index, size, sorted(members)) : state_max_ability
    memo = {}
    def calc_max(idx, size, members):
        # 베이스 케이스
        # size(팀 크기)가 목표 값(k)에 달하면, 구성원의 고유 능력치와 증감폭을 전부 더해 반환
        if size == k:
            return sum(data[m][n] for m in members for n in members)
        # 상태 최적해가 존재하면, 그 값을 반환
        if (idx, size, tuple(sorted(members))) in memo:
            return memo[idx, size, tuple(sorted(members))]

        # 최댓값 변수 초기화(음의 무한대)
        max_ab = float("-inf")
        
        # 현재 고려 중인 선수(idx)를 포함하여 그 이후 번호의 선수들을 구성하는 재귀적 호출
        # 계산이 끝나면(반환되면), 해당 선수를 제외하고 그 다음 선수부터 같은 동작을 수행해 최댓값 업데이트
        for i in range(idx, N):
            max_ab = max(max_ab, calc_max(i+1, size+1, members + [i]))

        # for loop 종료 후, 현재 상태 최적해 기록
        memo[(idx, size, tuple(sorted(members)))] = max_ab

        return max_ab  # 최적해 반환

    # 초기 값부터 모든 선수에 대해 크기가 k인 팀을 구성
    # 마지막 선수(N-1)까지 고려한 상태 최적해 반환
    answer = calc_max(0, 0, [])
    return answer

# 출력 파트
print(solution(data, N, k))