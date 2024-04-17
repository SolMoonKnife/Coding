from heapq import  heapify
# 최소 힙을 만들어줌
arr = [3, 1, 4, 8, 5, 9, 5]
heapify(arr)
print(arr)

# 최대 힙이 필요하다면?
# 리스트를 모두 음수로 바꿔서 최소 힙으로 만든 다음 다시 양수로 바꾼다
max_arr = [-x for x in arr]
heapify(max_arr)
max_arr = [-x for x in max_arr]
print(max_arr)
