solution = lambda n: next(e for e in range(1, n) if n % e == 1)

for i in range(3, 324, 11):
    print(i, solution(i))

# next : eterable한 객체의 각 요소를 순서대로 반환하는 함수
# 만일 연산을 통해 eterable을 생성하는 경우 각 순서까지만 연산하도록 만든다.
# next를 반복해서 사용할 경우 1, 2, 3, ... 번 순서의 요소를 반환한다.