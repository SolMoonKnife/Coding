# 1~73회 기본 확률 0.6%
# 74회부터 회당 6%p 증가
# 89회에 96.6%, 90회에 100%
import numpy as np
import math as mt
import time as tm
def gacha(n):
    rate = lambda x: 1.0 if x == 90 else 0.006 + (0 if x < 74 else 0.06 * (x - 73))
    stack = 0
    mustup = 0
    win = [0, 0]
    pickdown, pickup = 0, 0
    while n > 0:
        stack += 1
        key = np.random.rand()
        if rate(stack) >= key:
            if mustup == 1:
                mustup = 0
                pickup += 1
            else:
                picksel = np.random.rand()
                if 0.5 >= picksel:
                    pickup += 1
                    win[0] += 1
                else:
                    mustup = 1
                    pickdown += 1
                    win[1] += 1
            stack = 0
        n -= 1
    return pickup, pickdown, win

def gacha_idle(n, x, r):
    # n : 시행 횟수 / x : 보장 횟수 / r : 독립 시행 확률
    # 이항 계수
    nCk = lambda n, k: mt.factorial(n) / (mt.factorial(k) * mt.factorial(n-k))  # n! / k! * (n-k)!

    # 독립 시행 확률
    return sum(nCk(n, k) * (r ** k) * ((1-r) ** (n-k)) for k in range(x, n+1))

print(
    "가챠 스택에 따른 확률은 다음 공식에 따라 연산됩니다.",
    "\nrate = 1.0 if x == 90 else 0.006 + (0 if x < 74 else 0.06 * (x - 73))",
    "\n90스택일 경우 100% / 1 ~ 73스택일 경우 0.6% / 74 ~ 89스택일 경우 0.6% + 73초과 스택 당 6%",
    "\n매번 독립 시행 시 key값을 무작위로 설정합니다. 범위: 0.0 ~ 1.0",
    "\nkey값이 스택에 따른 확률보다 작은 값인 경우 ★★★★★ 등장으로 간주합니다.",
    "\n★★★★★ 등장 시 확정 천장일 경우 픽업 아이템이 등장합니다.",
    "\n★★★★★ 등장 시 확정 천장이 아닐 경우 픽업 key값을 무작위로 설정합니다. 범위: 0.0 ~ 1.0",
    "\n픽업 key값이 0.5이하인 경우 픽업 아이템이 등장하고, 0.5초과인 경우 픽뚫 아이템이 등장합니다.",
    "\n픽뚫 아이템이 등장한 경우 다음 ★★★★★ 등장 시 확정 천장으로 설정됩니다.\n"
)

TRY = 1000000000
start = tm.time()
x, y, win = gacha(TRY)
end = tm.time()
print(f"시행 {TRY}회, 연산 시간 {(end - start):.{4}f}초")
print(f"유라 {x}개, 픽뚫 {y}개")
print(f"유라 획득 확률: {100*x/TRY}%")
print(f"★★★★★ 획득 확률: {100*(x+y)/TRY}%")
