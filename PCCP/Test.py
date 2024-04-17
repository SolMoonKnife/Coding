def solution(before, after):
    stack = [c for c in before]
    compare = [c for c in after]
    flag = 0
    while stack:
        flag = 0
        pre = stack.pop(0)
        for i in range(len(compare)):
            if compare[i] == pre:
                flag = 1
                compare.pop(i)
                break
        else:
            break
    return flag


print(solution("olleh", "hello"))