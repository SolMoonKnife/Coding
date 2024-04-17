def mergeSort(A, p, r):
    def merge(x, y, z):  # 합집합과 병합(merge)의 차이: 중복을 허용하면 병합이고, 허용하지 않으면 합집합
        # 구간 참고: [x    y][y+1   z]
        # posA: A의 병합 위치
        # posFront, posRear: 각 부분 배열의 병합되지 않은 값 중, 최솟값의 위치
        posA, posFront, posRear = x, x, y+1

        # 배열 원본 복사
        C = list(A)

        # 전/후반 배열 둘 중 어느 하나를 모두 병합할 때까지
        while posFront <= y and posRear <= z:
            if C[posFront] < C[posRear]:
                A[posA] = C[posFront]
                posFront += 1
            else:
                A[posA] = C[posRear]
                posRear += 1
            posA += 1

        # 전반이 끝났으면 후반, 후반이 끝났으면 전반 배열의 남은 모든 원소를 병합
        if posFront > y:
            while posRear <= z:
                A[posA] = C[posRear]
                posA += 1
                posRear += 1
        elif posRear > z:
            while posFront <= y:
                A[posA] = C[posFront]
                posA += 1
                posFront += 1

    if p < r:
        q = (p + r)//2
        # 분할
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        # 병합
        merge(p, q, r)

from numpy import random as nprd
A = [int(100*nprd.rand()) for _ in range(100)]

print("Original:")
for i in range(100):
  if i%10 == 0 and i != 0: print()
  print(f"{A[i]:02d}", end=' ')

mergeSort(A, 0, len(A)-1)

print("\nMerged:")
for i in range(100):
  if i%10 == 0 and i != 0: print()
  print(f"{A[i]:02d}", end=' ')

# 시간 복잡도는 결국 입력에 다른 소요시간을 나타내므로, 2개 이상의 입력이 영향을 준다면
# 두 개 이상의 변수에 대한 함수로 표현해도 된다. 단, 두 변수 사이에 대수적인 관계(대소관계 포함)가 있다면,
# 하나의 변수로 묶어서 표현할 수 있을 것이다. 예를 들어 m < 2n이라면, O(m+n)은 O(3n) = O(n)이라고 표현해도 무방할 것이다.

# n에 대한 로그함수복잡도와 지수함수복잡도를 비교하려면 로그함수를 k로 치환하고 n을 k에 대한 식으로 표현하여 비교한다.
# k = log n 이면, n = 2^k

# 점근적 시간 복잡도 분석 방법을 병렬처리(parallel processing)의 관점에서 논의하라.
# -> 아무리 프로세서(코어)개수를 늘려도, 상수 개의 코어이다.
# -> 한 번에 상수 개의 연산을 처리하여 함수를 상수로 나누더라도, 점근적 시간 복잡도 분석은 여전히 유효하다.