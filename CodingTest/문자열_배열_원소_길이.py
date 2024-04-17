strlist = ["We", "are", "the", "world!"]

solution_1 = lambda l: [len(x) for x in l]
solution_2 = lambda l: list(map(len, l))

print(solution_1(strlist))
print(solution_2(strlist))