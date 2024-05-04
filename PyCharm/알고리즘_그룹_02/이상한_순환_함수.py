def min_idx(a, s, e):
    idx, val = -1, float("inf")
    for i in range(s, e+1):
        if a[i] < val:
            idx, val = i, a[i]
    return idx


def fun9(a, s, e):
    if s >= e:
        return
    min_index = min_idx(a, s, e)

    temp = a[s]
    a[s] = a[min_index]
    a[min_index] = temp

    fun9(a, s+1, e)

test = [4, 6, 8, 2, 1, 3]
fun9(test, 0, 5)
print(test)
