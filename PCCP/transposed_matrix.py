matrix = [
    [3,7,9],
    [4,2,6],
    [8,1,5]
]

for r in range(3):
    for c in range(3):
        if r > c:
            (matrix[r][c], matrix[c][r]) = (matrix[c][r], matrix[r][c])
            # 조건문이 없다면? 전치 후 다시 전치하여 원상 복구된다!!

print(matrix)

