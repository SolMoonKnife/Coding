def insertionSort(A, n):
    for i in range(n):
        target = A[i]
        idx = 0
        while A[idx] < target and idx < i:
            idx += 1
        if i != idx:
            for k in range(i, idx-1, -1):
                A[k] = A[k-1]
            A[idx] = target

A = [8, 3, 6, 4, 5, 2, 98, 3, 6, 4, 5, 2, 98, 3, 6, 4, 5, 2, 9]
insertionSort(A, len(A))

print(A)
