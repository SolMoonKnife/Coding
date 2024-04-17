# 1 by 1부터, 찾는 숫자 위치를 반환하는 델타 탐색 함수

def delta_search(mat, num):
    x, y = 0, 0
    rows, cols = len(mat), len(mat[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == num:
                return r, c

            for i in range(4):
                (new_r, new_c) = (r + dx[i], c + dy[i])

                if (0 <= new_r < rows) and (0 <= new_c < cols) and (mat[new_r][new_c] == num):
                    return new_r, new_c
    return None

matrix = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

print(delta_search(matrix, 7))
