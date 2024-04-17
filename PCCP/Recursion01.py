# 재귀를 사용하여 자연수의 숫자합을 구하는 sum_all 함수를 만들어라.
# 재귀 구조 : 종료 조건, 점화식
def sum_all(num):
    if num == 1:
        return 1
    return num + sum_all(num - 1)

print(sum_all(10))
