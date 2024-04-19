# 1~73회 기본 확률 0.6%
# 74회부터 회당 6%p 증가
# 89회에 96.6%, 90회에 100%
import numpy as np
import math as mt
import time as tm
def gacha(n, pickupRate=0.5, type="C"):
    rate = lambda x: 1.0 if x == 90 else 0.006 + (0 if x < 74 else 0.06 * (x - 73))
    rate_core = lambda x: 1.0 if x == 80 else 0.006 + (0 if x < 64 else 0.06 * (x - 63))
    stack = 0
    mustup = 0
    win = [0, 0]
    pickdown, pickup = 0, 0
    if type == "C":
        while n > 0:
            stack += 1
            key = np.random.rand()
            if rate(stack) >= key:
                if mustup == 1:
                    mustup = 0
                    pickup += 1
                else:
                    picksel = np.random.rand()
                    if pickupRate >= picksel:
                        pickup += 1
                        win[0] += 1
                    else:
                        mustup = 1
                        pickdown += 1
                        win[1] += 1
                stack = 0
            n -= 1
    elif type == "L":
        while n > 0:
            stack += 1
            key = np.random.rand()
            if rate_core(stack) >= key:
                if mustup == 1:
                    mustup = 0
                    pickup += 1
                else:
                    picksel = np.random.rand()
                    if pickupRate >= picksel:
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
    "TRY = 시행 횟수\n" +
    "PICKUP_RATE = 픽업 확률\n" +
    "PICKUP_TYPE = 픽업 유형(캐릭터 \"C\" / 광추 \"L\")\n"
)

TARGET = "반디 전광"
TRY = 70
PICKUP_RATE = 0.75
PICKUP_TYPE = "L"

start = tm.time()
x, y, win = gacha(TRY, PICKUP_RATE, PICKUP_TYPE)
end = tm.time()

print(f"시행 {TRY}회, 연산 시간 {(end - start):.{4}f}초")
print(f"{TARGET} {x}개, 픽뚫 {y}개 (픽업 확률 {(PICKUP_RATE*100):.{1}f}%)")
print(f"{TARGET} 획득 확률: {100*x/TRY}%")
print(f"★★★★★ 획득 확률: {100*(x+y)/TRY}%")
