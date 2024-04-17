# 입력 파트
N = int(input())

# 함수 파트
def solution(N):
    # 이진 수열의 개수를 저장하는 변수
    global_count = 0

    # 조건을 만족하는 이진 수열을 만드는 함수
    def mkseq(previous=-1, count=0):
        nonlocal global_count

        # 만든 이진 수열의 길이가 충족되면 이진 수열의 개수를 증가시킴
        if count >= N:
            global_count += 1
            return

        # 이전에 추가된 수가 0이 아닌 경우에만 0을 추가한 이진 수열 생성
        if previous != 0:
            mkseq(0, count + 1)
        mkseq(1, count + 1)

    # 모든 이진 수열 생성
    mkseq()

    return global_count

# 출력 파트
print(solution(N))
