def solution(the_list):
    j = len(the_list)
    while j > 1:
        maximum, index = 0, 0
        for i in range(j):
            (maximum, index) = (the_list[i], i) if the_list[i] > maximum else (maximum, index)
        the_list[j-1], the_list[index] = the_list[index], the_list[j-1]  # swap
        j -= 1
    return the_list

data = [3, 6, 1, 8, 4, 9, 10, 2]
print(solution(data))