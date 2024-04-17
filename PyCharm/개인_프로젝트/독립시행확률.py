import math as mt

values = input("RATE COUNT PICKUP : ").split()
RATE, COUNT, PICKUP = float(values[0]), int(values[1]), int(values[2])

def gacha(n, x, r):
    # n : 시행 횟수 / x : 보장 횟수 / r : 독립 시행 확률
    # 이항 계수
    nCk = lambda n, k: mt.factorial(n) / (mt.factorial(k) * mt.factorial(n-k))  # n! / k! * (n-k)!

    # 독립 시행 확률
    return sum(nCk(n, k) * (r ** k) * ((1-r) ** (n-k)) for k in range(x, n+1))

print(f"{COUNT}회 뽑기에서 {RATE*100}% 확률로 최소 {PICKUP}번 등장할 확률은?")
print(f"{100 * gacha(COUNT, PICKUP, RATE):.{4}f}%")

input("\nPress Enter to Exit")

