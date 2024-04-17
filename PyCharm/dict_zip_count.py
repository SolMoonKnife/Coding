n = 0
control = "wsdawsdassw"

solution = lambda n, s: (d := {'w':1, 's':-1, 'd':10, 'a':-10}) and sum(d[c] for c in s) + n

result = solution(n, control)

print(result)

# 딕셔너리 쉽게 만드는 팁 : zip 함수 사용
key = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
print(key)

# 문자열에 문자가 포함된 개수를 세는 count
count_d = control.count('d')
print(count_d)