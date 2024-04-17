from numpy import random as rd
from time import time as tm

def mergeSort(A, p, r):

    # 정렬 구간의 크기가 1이 될 때까지 재귀 호출
    if p < r:
        q = (p + r)//2          # 구간 중간 계산
        mergeSort(A, p, q)      # 처음부터 중간까지
        mergeSort(A, q+1, r)    # 중간 다음부터 마지막까지
        merge(A, p, q, r)       # 정렬된 두 구간 병합 정렬

def merge(A, p, q, r):
    n = r - p + 1
    tmp = [0] * n

    (k, i, j) = (0, p, q+1)

    while i <= q and j <= r:
        if A[i] < A[j]:
            tmp[k] = A[i]
            i += 1
        else:
            tmp[k] = A[j]
            j += 1
        k += 1

    while i <= q:
        tmp[k] = A[i]
        k, i = k + 1, i + 1

    while j <= r:
        tmp[k] = A[j]
        k, j = k + 1, j + 1

    for l in range(n):
        A[l + p] = tmp[l]

N = 30000
A = [int(10000*rd.rand()) for _ in range(N)]

print("Original:", A)
start = tm()
mergeSort(A, 0, N-1)
end = tm()
print("Sorted:", A)
print("time:", f'{end-start:.{30}f}')
