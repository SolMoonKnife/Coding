arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2], [0, 3, 2], [0, 2, 2]]

def solution(arr, queries):
    answer = []
    for (s, e, k) in queries:
        sorted_arr, flag = sorted(arr[s:e+1]), -1
        for i in sorted_arr:
            if i > k:
                flag = i
                break
        answer.append(flag)
    return answer

print(solution(arr, queries))