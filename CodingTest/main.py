solution = lambda str1, str2: 1 if any(str1[i:i+len(str2)] == str2 for i in range(len(str1) - len(str2) + 1)) else 2

n = 34499761
print(n ** 0.5)
print(n / n ** 0.5)