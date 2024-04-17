with open("harry_full.txt", "r") as file:
    harry = list(file.read().split())

def bubbleSort(A):
    n = len(A)
    for last in range(n-1, -1, -1):
        for i in range(last):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

def insertionSort(A):
    n = len(A)
    for i in range(n):
        target = A[i]
        idx = 0
        while A[idx] < target and idx < i:
            idx += 1
        if i != idx:
            for k in range(i, idx, -1):
                A[k] = A[k-1]
            A[idx] = target

def mergeSort(A, p, r):

    if p < r:
        q = (p + r)//2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

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

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[r], A[i + 1] = A[i + 1], A[r]

    return i + 1

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

def heapSort(A):
    n = len(A)
    buildHeap(A, n)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        percolateDown(A, 0, i)

import time as t
import sys

sys.setrecursionlimit(10000)  # 퀵소트에 재귀 심도가 부족하여 확장하였습니다.

harryForBubble = harry.copy()
harryForInsert = harry.copy()
harryForMerges = harry.copy()
harryForQuicks = harry.copy()
harryForHeapso = harry.copy()
harryForLibray = harry.copy()

bubble_start = t.time()
bubbleSort(harryForBubble)
bubble_end = t.time()
print(f"BubbleSort:  \t{(bubble_end - bubble_start):.{24}f}")

insert_start = t.time()
insertionSort(harryForInsert)
insert_end = t.time()
print(f"InsertionSort:\t{(insert_end - insert_start):.{24}f}")

merge_start = t.time()
mergeSort(harryForMerges, 0, len(harryForMerges) - 1)
merge_end= t.time()
print(f"MergeSort:   \t{(merge_end - merge_start):.{24}f}")

quick_start = t.time()
quickSort(harryForQuicks, 0, len(harryForQuicks) - 1)
quick_end = t.time()
print(f"QuickSort:   \t{(quick_end - quick_start):.{24}f}")

heap_start = t.time()
heapSort(harryForHeapso)
heap_end = t.time()
print(f"HeapSort:    \t{(heap_end - heap_start):.{24}f}")

sort_start = t.time()
harryForLibray.sort()
sort_end = t.time()
print(f"TimSort:     \t{(sort_end - sort_start):.{24}f}")

'''
BubbleSort:  	819.350606918334960937500000
InsertionSort:	481.172449588775634765625000
MergeSort:   	0.360476493835449218750000
QuickSort:   	3.255778551101684570312500
HeapSort:    	0.450885534286499023437500
TimSort:  	    0.023026227951049804687500
'''