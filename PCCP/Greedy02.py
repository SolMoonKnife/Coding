# 어떤 수에서 k개의 숫자를 제거하고 그대로 배열한 수 중에 가장 큰 수 문자열로 반환
# 수는 문자열, k는 정수로 입력

# 탐욕법 : 지역적으로 최적해를 찾으려는 접근법으로 문제를 해결할 수 있는 기법
# 모든 경우에 가능하지는 않으므로 탐욕법 접근이 문제 전체의 최적해를 도출하는지 분석이 필요하다.

def solution(number, k):
    stack = []
    for i, num in enumerate(number):
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        if k == 0:
            stack += number[i:]
            break
        stack.append(num)

    stack = stack[:-k] if k > 0 else stack
    answer = ''.join(stack)

    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))

