id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    
    report = list(set(report)) # 중복을 제거한 리스트로 다시 만든다!!
    num = len(id_list)

    # 유저 간의 신고자-피신고자 관계를 행렬로 정리한다.
    user_relation = [[0]*num for _ in range(num)]

    for i in range(len(report)):
        reporter, reported = report[i].split()
        user_relation[id_list.index(reporter)][id_list.index(reported)] = 1

    answer = [0] * num
    for c in range(num):
        cnt = 0
        for r in range(num):
            cnt += user_relation[r][c]
            if cnt >= k:
                for r in range(num):
                    answer[r] = user_relation[r][c]
                break
    return answer

solution(id_list, report , k)
