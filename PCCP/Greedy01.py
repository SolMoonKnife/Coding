def solution(n, lost, reserve):
    # n      : 학생 수
    # lost   : 잃어버린 학생 리스트
    # reserve: 여벌 있는 학생 리스트
    able = 0
    students = [0] + [1 for _ in range(n)]
    for r in reserve:
        students[r] += 1

    for l in lost:
        students[l] -= 1

    for s in range(1, n+1):
        # 1번부터 n번까지 학생에 대하여
        if students[s] == 0:
            # 체육복이 없으면 앞, 뒤를 확인하여 빌릴 수 있으면 빌린다
            if students[s - 1] == 2:
                students[s], students[s - 1] = 1, 1
            elif (s < n) and students[s + 1] == 2:
                students[s], students[s + 1] = 1, 1

    for i in students:
        if i > 0: able += 1

    print(students)

    return able

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))

