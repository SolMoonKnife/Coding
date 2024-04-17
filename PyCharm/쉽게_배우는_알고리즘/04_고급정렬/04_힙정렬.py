# 완전이진트리배열의 부모 인덱스는 (k-1)//2, 자식 인덱스는 (2k, 2k+1)

# 배열을 힙으로 만드는 함수
# 부모 노드 k에 대하여 하강 침투(스며내리기): For the tree that index of root-node is 0.
def percolateDown(A, k, n):
    child = 2 * k + 1
    right = 2 * k + 2
    if child < n:
        if right < n and A[child] < A[right]:
            child = right
        if A[k] < A[child]:
            A[k], A[child] = A[child], A[k]
            percolateDown(A, child, n)
def buildHeap(A, n):
    for i in range(len(A)//2, -1, -1):
        percolateDown(A, i, n)

# def deleteHeap(A):
#     tmp = A[0]
#     if len(A) > 1:
#         A[0] = A.pop()
#         buildHeap(A)
#     else: A.pop()
#     return tmp

def heapSort(A):
    n = len(A)
    buildHeap(A, n)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        percolateDown(A, 0, i)


heap = [4, 6, 7, 10, 1, 19, 3, 7, 5, 17]
print(heap)
heapSort(heap)
print(heap)