def solution(numbers):
    nums = []

    while numbers:
        max = 0
        for i in range(len(numbers)):
            n = str(numbers[i])  # 정수의 문자화
            c = n[0]  # 최대 자리 수 문자 추출
            s = int(c)  # 다시 정수화
            if s > numbers[max]:
                max = i
        nums.append(str(numbers.pop(max)))

    answer = "".join(nums)

    return answer

print(solution([3, 30, 34, 5, 9]))