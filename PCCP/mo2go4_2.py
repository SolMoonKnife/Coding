id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2


def solution(id_list, report, k):
    report = set(report)
    answer = [0]*len(id_list)
    report_counts = {user:0 for user in id_list}

    for rep in report:
        _, e = rep.split()
        report_counts[e] += 1
    for rep in report:
        s, e = rep.split()
        if report_counts[e] >= k:
            answer[id_list.index(s)] += 1

    return answer