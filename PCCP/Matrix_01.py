matrix = [
    [3,7,9],
    [4,2,6],
    [8,1,5]
]

# 모든 원소의 합을 구하는 sum_matrix() 만들기
# matrix를 순회하며 더하는 방식으로 만들자

def sum_matrix(mat):
    sum = 0
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            sum += mat[r][c]
    return sum

print(sum_matrix(matrix))
