def selectionSort(A, n):
    for i in range(n-1, -1, -1):
        m = max(A[:i+1])
        A[A.index(m)], A[i] = A[i], A[A.index(m)]

B = [4, 7, 2, 5, 1]
selectionSort(B, len(B))

print(B)
