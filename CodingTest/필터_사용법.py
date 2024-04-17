solution = lambda n: sum(filter(lambda n: n % 2 == 0, range(n+1)))

print(solution(10))
# n 이하의 짝수의 합을 반환하는 함수. 필터를 사용해 iterable한 수열에서 짝수만 걸렀다. (굳이긴 함)