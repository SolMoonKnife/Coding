# 입력 파트
N = int(input())
sequence = list(map(int, input().split()))

# 함수 파트
def judgeSequence(N, sequence, idx=0):
    # 마지막 수에 도달 "Yes" 반환
    if idx == N-1:
        return "Yes"

    num = sequence[idx]

    # 0에 도달 "No" 반환
    if num == 0:
        return "No"

    # Boolean 대신 "Yes"또는 "No"값을 통해 재귀적 탐색 수행
    for moves in range(1, num+1):
        # 해당 심도에서 탐색에 성공 "Yes"반환
        if judgeSequence(N, sequence, idx + moves) == "Yes":
            return "Yes"
    
    # 해당 심도에서 탐색에 실패 "No"반환
    return "No"

# 출력 파트
print(judgeSequence(N, sequence))
