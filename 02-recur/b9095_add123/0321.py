import sys
sys.stdin = open("add123.txt", "r")

T = int(input())
def sum_123(i):
    if dp[i]:
        return dp[i]

    dp[i] = sum_123(i-3) + sum_123(i-2) + sum_123(i-1)
    # 큰 숫자가 앞에 있으면 더 빨라질듯 - 주희
    return dp[i]

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for tc in range(1, T+1):
    n = int(input())

    print(sum_123(n))