# Partition Problem: 주어진 집합을 합이 같은 두 개의 집합으로 나눌 수 있는가?

arr = [2, 3, 4, 5]

def solution(arr):
    if sum(arr) % 2 != 0:
        return False

    targetSum = sum(arr) // 2
    targetSubset = []

    def backtrack(idx):
        if sum(targetSubset) == targetSum:
            print(targetSubset)
            return True
        elif sum(targetSubset) > targetSum:
            return False
        # 중단 조건 완료

        # 백트래킹
        for i in range(idx, len(arr)):
            # 다음 원소들을 부분 집합에 삽입해보기 (포함)
            targetSubset.append(arr[i])

            # 최대 심도까지 탐색
            if backtrack(i+1):
                return True

            # 탐색 실패: 해당 원소 제거 (미포함)
            targetSubset.pop()

        return False

    return backtrack(0)

print(solution(arr))

#  정답: [2, 5] [3, 4]