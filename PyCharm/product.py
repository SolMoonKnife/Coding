from itertools import product
def solution(mn, mx):
    answer = []
    for i in range(mn, mx+1):
        answer += ["".join(p) for p in product(['0', '5'], repeat=i)]
    deduplication = sorted(list(set(map(int, answer))))
    return list(filter(lambda x: len(str(x)) >= mn, deduplication))

def solution_2(mn, mx):
    answer = [int("".join(p)) for i in range(mn, mx+1) for p in product(['0', '5'], repeat=i)]
    deduplicated = sorted(filter(lambda x: len(str(x)) >= mn, answer))
    return deduplicated


print(solution(2, 4))
print(solution_2(2, 4))

# iterable한 요소에서 조합 가능한 모든 경우의 수 반환
# 5또는 0으로만 이루어진 모든 수를 반환 (최소길이mn, 최대길이mx)

# filter 사용법
original_list = ['apple', 'banana', 'kiwi', 'grape', 'orange']
milestone = 5

filtered_list = list(filter(lambda x: len(x) >= milestone, original_list))
print(filtered_list)