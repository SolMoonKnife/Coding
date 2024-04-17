def func(lst, value, start = 0, end = -1):
    if end == -1:
        end = len(lst) - 1

    mid = (end + start)//2
    if lst[mid] < value:
        print(f'탐색(s) [{start} : {end}], mid : {mid}')
        return func(lst, value, mid+1, end)
    elif lst[mid] > value:
        print(f'탐색(b) [{start} : {end}], mid : {mid}')
        return func(lst, value, start, mid)
    return mid

sample = [1, 3, 4, 7, 8, 10, 11]
target = 10
answer = func(sample, target)

print(f"찾은 인덱스 : {answer}, sample[{answer}] : {sample[answer]}")
