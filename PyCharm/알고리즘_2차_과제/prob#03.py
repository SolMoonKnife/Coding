import random
import time
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def delete_max(self):
        if not self.queue:
            return None

        max_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i] > self.queue[max_index]:
                max_index = i

        self.queue[max_index], self.queue[-1] = self.queue[-1], self.queue[max_index]
        return self.queue.pop()


class PriorityQueueMaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, -value)  # 최소 힙을 최대 힙으로 사용하기 위해 음수로 저장

    def delete_max(self):
        if not self.heap:
            return None
        return -heapq.heappop(self.heap)  # 삭제 연산 시 음수인 값을 양수로 변환

N = 100000
M = 100000

# 측정용 리스트 생성
A = [random.randint(0, N) for _ in range(N)]
B = [random.randint(0, N) for _ in range(N)]
C = B.copy()

# PriorityQueue 시간 측정
pq = PriorityQueue()
start = time.time()
for i in range(M):
    operation = random.choice(["insert", "delete_max"])
    if operation == "insert":
        value = B.pop()
        pq.insert(value)
    else:
        pq.delete_max()
end = time.time()
print("PriorityQueue 측정 시간:", end - start)

# PriorityQueueMaxHeap 시간 측정
pq_max_heap = PriorityQueueMaxHeap()
start = time.time()
for i in range(M):
    operation = random.choice(["insert", "delete_max"])
    if operation == "insert":
        value = C.pop()
        pq_max_heap.insert(value)
    else:
        pq_max_heap.delete_max()
end = time.time()
print("PriorityQueueMaxHeap 측정 시간:", end - start)

''' 특정 수행 결과
PriorityQueue 측정 시간: 0.43953871726989746
PriorityQueueMaxHeap 측정 시간: 0.05580449104309082
'''
