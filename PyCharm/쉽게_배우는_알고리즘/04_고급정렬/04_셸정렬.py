def shellSort(A):
    gap = len(A) // 2
    gaps = []
    while gap > 0:
        gaps.append(gap)
        gap //= 2

    if gaps[-1] != 1:
        gaps.append(1)

    def _stepInsertionSort(A, k, h):
        n = len(A)
        for i in range(k+h, n, h):
            newItem = A[i]

            while True:
                pass

                break

            for j in range(i - h, -1, -h):
                if newItem < A[j]:
                    A[j + h] = A[j]
                else: break
            A[i] = newItem

    for h in gaps:
        for k in range(0, h):
            _stepInsertionSort(A, k, h)


def insertionSort(A):
    n = len(A)
    for i in range(n):
        target = A[i]
        idx = 0
        while A[idx] < target and idx < i:
            idx += 1
        if i != idx:
            for k in range(i, idx - 1, -1):
                A[k] = A[k - 1]
            A[idx] = target



import time as t
import numpy as np

o = [int(np.random.rand() * 1000) for _ in range(10)]
l = o.copy()
m = o.copy()

print(o)

start = t.time()
shellSort(l)
end = t.time()
print(f"{(end - start):.{24}f}")

start = t.time()
insertionSort(m)
end = t.time()
print(f"{(end - start):.{24}f}")

print(l)
print(m)