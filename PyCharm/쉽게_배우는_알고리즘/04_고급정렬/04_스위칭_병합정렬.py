from numpy import random as rd
from time import time as tm

def switchMergeSort(A):
    B = [0]*len(A)
    for i in range(len(A)):
        B[i] = A[i]
    swt_ms(0, len(A)-1, A, B)

def swt_ms(p, r, A, B):
    if p < r:
        q = (p + r) // 2
        swt_ms(p, q, B, A)
        swt_ms(q+1, r, B, A)
        switchMerge(p, q, r, B, A)

def switchMerge(p, q, r, ref, tar):
    i, j, k = p, q+1, p

    while i <= q and j <= r:
        if ref[i] < ref[j]:
            tar[k] = ref[i]
            i, k = i + 1, k + 1
        else:
            tar[k] = ref[j]
            j, k = j + 1, k + 1

    while i <= q:
        tar[k] = ref[i]
        i, k = i + 1, k + 1

    while j <= r:
        tar[k] = ref[j]
        j, k = j + 1, k + 1

N = 30000
A = [int(10000*rd.rand()) for _ in range(N)]

print("Original:", A)
start = tm()
switchMergeSort(A)
end = tm()
print("Sorted:", A)
print("time:", f'{end-start:.{30}f}')
