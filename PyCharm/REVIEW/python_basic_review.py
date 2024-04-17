#01 프로덕트(product) : 후보(리스트)에서 선택하여 만들 수 있는 모든 순열을 반환함
print("#01 프로덕트")
from itertools import product
print(list(product(['A', 'B', 'C'], repeat=2)))  	# 전달된 iterable을 repeat번 반복하는 순열을 반환한다.
print(list(product([1, 2, 3], ['a', 'b'])))  		# 전달된 iterable에서 각각 하나의 원소를 꺼내 만든 순열을 반환한다.
print(list(product([4, 5], ['x', 'y'], repeat=3)))  # 여러 iterable에서 만든 순열을 iterable로 삼아 반복하는 순열을 반환.

#02 소수점 표기법 : f-문자열을 활용하여 소수점 자릿수를 축소하거나 확장함
print("\n#02 소수점 표기법")
fnum = 1.23456789
print(f"{fnum:.{3}f}")   # 소수 3자리까지 표시, 축소되는 경우 4자리에서 반올림	# 1.235
print(f"{fnum:.{10}f}")  # 소수 10자리까지 표시, 부족한 만큼 0을 붙임		# 1.2345678900

#03 enumerate : 반복 가능한(iterable)객체를 받아 인덱스와 해당 요소를 튜플로 반환한다.
print("\n#03 enumerate()")
enumerate_items = ['apple', 'banana', 'kiwi', 'grape', 'mango']

# 1. 인덱스와 요소를 출력하기
for i, e in enumerate(enumerate_items):
    if i == 0: print("[index]\t[item]")
    print(f"{i}\t\t{e}")

# 2. 임의의 시작 인덱스를 정해서 출력하기
for i, e in enumerate(enumerate_items, start=1):
    if i == 1: print("[index]\t[item]")
    print(f"{i}\t\t{e}")

# 3. 딕셔너리 만들기 -> O(n) 시간복잡도 소요
idx_dict = dict(enumerate(enumerate_items))
print(idx_dict)  # {0: 'apple', 1: 'banana', 2: 'kiwi'}

# 4. 인덱스 조건에 따라 값 추출하기 (짝수 인덱스만 추출하기)
enumerate_even_items = list(e for i, e in enumerate(enumerate_items) if i % 2 == 0)
print(enumerate_even_items)

# 5. 인덱스 조건에 따라 값 업데이트하기(홀수 인덱스만 대문자화)
enumerate_odd_upper = list((e if i % 2 == 0 else e.upper()) for i, e in enumerate(enumerate_items))
print(enumerate_odd_upper)

#04 next : 반복(iter)객체의 요소를 순서대로 하나씩 반환한다. # 다른 객체는 iter() 변환이 선행되어야 함
print("\n#04 next()")
next_numbers = [1, 2, 3, 4, 5]
iterator_numbers = iter(next_numbers)
for _ in range(len(next_numbers)):
    print(next(iterator_numbers), end=' ')

# 디폴트 값 설정 (다음 값이 없는 경우 디폴트 값 사용)
print(next(iterator_numbers, "No more numbers"))

# 다음 값이 없으면 루프 탈출
iterator_numbers_2 = iter(next_numbers)
while True:
    try:
        print(next(iterator_numbers_2), end=' ')
    except StopIteration:
        print("No more numbers(2)")
        break

# 무한 시퀀스 제너레이터
def next_generator(value = 0):
    while True:
        yield value  # 값을 반환하고 다음 호출까지 대기
        value += 1   # 다음 호출 시 연산됨

infinite_sequence = next_generator(1)  # 1부터 시작하는 무한 시퀀스 생성
for _ in range(30):
    print(next(infinite_sequence), end=' ')  # 호출할 때마다 연산하여 다음 값을 생성함
print()
    
# n을 나눈 나머지가 1인 가장 작은 원소 추출하기 : 가능한 것중 첫 번째 요소를 찾으면 연산을 중단한다
first_rest_1 = lambda n: next((e for e in range(1, n) if n % e == 1), n-1)  # 최대 n-1이 나오지만, 명시적 예외 처리하였음
print('53을 나눈 나머지가 1인 가장 작은 수:', first_rest_1(53))
print('438을 나눈 나머지가 1인 가장 작은 수:', first_rest_1(438))
print('2226을 나눈 나머지가 1인 가장 작은 수:', first_rest_1(2226))

#05 zip() : 여러 개의 iterable 객체에 대하여 같은 인덱스 요소끼리 묶은 튜플을 요소로 하는 iterable 객체를 반환한다.
print("#05 zip()")

listForZip01 = [1, 2, 3]
listForZip02 = ['one', 'two', 'three']
# iterator 사용 시 주의 사항 : iterator는 한번 소비되면 재사용될 수 없다.
# 변수를 통해 참조하여도 사용할 수 있으나, 소비되면 재사용할 수 없으므로 참조는 필요하지 않다.

print(dict(zip(listForZip01, listForZip02)))
print(list(zip(listForZip01, listForZip02)))

#06 이중 join() : 큰 덩어리를 구성하는 규칙 속 모든 원소에 대한 규칙을 정해 문자열을 만든다.
# 매트릭스 형식의 문자열 만들기
mat_str = "\n".join(" ".join(f"{e + 10*f:02d}" for e in range(1, 10)) for f in range(0, 10))
print(mat_str)

#07 이항 분포에 따른 독립 시행 확률 계산기
import math as mt
def gacha(n, x, r):
    # n : 시행 횟수 / x : 보장 횟수 / r : 독립 시행 확률
    # 이항 계수
    nCk = lambda n, k: mt.factorial(n) / (mt.factorial(n) * mt.factorial(n-k))
    # 독립 시행 확률
    return sum(nCk(n, k) * (r ** k) * (1-r ** (n-k)) for k in range(x, n+1))