# 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서
# 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
# 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

'''

최소자릿수와 최대자릿수 감지
0과 5로 이루어진 모든 가능한 문자열 생성
정수로 캐스팅하고 조합으로 변환
정렬하여 반환

'''
# product 사용법!!
from itertools import product
def solution(l, r):
    min_len = len(str(l))
    max_len = len(str(r))

    all_elem = []
    for i in range(min_len, max_len+1):
        all_elem += [''.join(p) for p in product(['0', '5'], repeat=i)]
    all_set = set([int(e) for e in all_elem if l <= int(e) <= r])

    return sorted(list(all_set))


print(solution(5, 555))