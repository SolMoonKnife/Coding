with open("input9.txt", "r") as file:
    file_contents = file.read()

file_list = [list(map(int, line.split())) for line in file_contents.split('\n')]

N = file_list[0][0]
data = file_list[1:N+1]
k = file_list[N+1][0]


def solution(A, N, k):
    memo = {}  # 메모이제이션을 위한 딕셔너리

    # 재귀적으로 팀을 구성하고 능력치를 계산하는 함수
    def calculate_max_ability(idx, count, members):
        # 기저 사례: 팀을 다 구성했을 때
        if count == k:
            # 팀의 능력치 총합을 계산하여 반환
            total_ability = sum(A[m][n] for m in members for n in members)
            return total_ability

        # 메모이제이션
        if (idx, count, tuple(sorted(members))) in memo:
            return memo[(idx, count, tuple(sorted(members)))]

        max_ability = float('-inf')
        # 팀원을 추가하여 재귀 호출
        for i in range(idx, N):
            max_ability = max(max_ability, calculate_max_ability(i + 1, count + 1, members + [i]))

        # 메모이제이션
        memo[(idx, count, tuple(sorted(members)))] = max_ability
        return max_ability

    # 처음부터 시작하여 최대 능력치를 구함
    max_ability = calculate_max_ability(0, 0, [])
    return max_ability

print(solution(data, N, k))  # 팀의 능력치 총합 출력
