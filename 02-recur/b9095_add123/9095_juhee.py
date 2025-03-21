import sys
sys.stdin = open("02-recur/b9095_add123/add123.txt", "r")

T = int(input())
def sum_123(i):
    if i == 1:
        return dp[1]
    if i == 2:
        return dp[2]
    if i == 3:
        return dp[3]
    dp[i] = sum_123(i-3) + sum_123(i-2) + sum_123(i-1)
    return dp[i]

for tc in range(1, T+1):
    n = int(input())
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    print(sum_123(n))
