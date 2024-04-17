# 파일 입력 파트
with open('input.txt', 'r') as file:
    file_content = file.read()

file_list = [list(map(int, line.split())) for line in file_content.split('\n')]

N = file_list[0][0]
W = file_list[1][0]
w = file_list[2]
v = file_list[3]

# 함수 파트
def solution(N, W, w, v):
    # 최적해 테이블 초기화
    bag = [[0 for _ in range(W+1)] for _ in range(N)]
    def bag_writer(item, weight):
        # 테이블을 벗어나면 0 반환
        if item < 0 or weight == 0:
            return 0
        
        # 해당 최적해가 이미 존재하면, 그 값을 반환
        if bag[item][weight] != 0:
            return bag[item][weight]

        # 현재 심도에서 아이템의 무게가 한도를 초과하면, 해당 아이템을 제외한 최적해 검색
        if weight < w[item]:
            result = bag_writer(item-1, weight)
        # 아니면, 현재 아이템을 포함한 것과 포함하지 않은 현재 무게에 대한 최적해 계산
        else:
            result = max(v[item] + bag_writer(item-1, weight-w[item]), bag_writer(item-1, weight))
        
        # 최적해를 테이블에 기록하고 반환
        bag[item][weight] = result
        return result
    # 마지막 아이템(N-1)까지 고려한 최적해 반환
    return bag_writer(N-1, W)

# 출력 파트
print(solution(N, W, w, v))
