n = 10
# 1부터 n까지의 합 출력

# 1.공식을 이용하기, 시간복잡도 1
print(int((1+n)*n/2))

# 2.for문을 이용하기, 시간복잡도 n
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)
