# 자연수 x에 대하여
# 현재 x가 짝수 : 2로 나누기
# 현재 x가 홀수 : 3x+1 로 바꾸기
# 해당 과정을 리스트로 나열하여 리턴
# x가 1이 될 때까지

def solution(n):
    answer = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        answer.append(int(n))
    return answer

print(solution(10))