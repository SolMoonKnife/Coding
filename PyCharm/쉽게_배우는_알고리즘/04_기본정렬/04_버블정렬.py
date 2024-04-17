def bubbleSort(A, n):
    for last in range(n-1, 0, -1):
        for i in range(last):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

A = [5, 3, 7, 8, 1, 4]
bubbleSort(A, len(A))

print(A)
