arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 1], [0, 3, 2], [0, 3, 3]]

def solution(arr, queries):
    for s, e, k in queries:
        for i in range(len(arr)):
            if i % k == 0 and s <= i <= e:
                arr[i] += 1
    return arr

print(solution(arr, queries))