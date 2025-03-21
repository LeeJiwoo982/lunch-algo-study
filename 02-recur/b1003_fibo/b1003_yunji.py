# def fibo(n):
#     f = [0] * (n + 1)
#     f[0] = 0
#     f[1] = 1

#     for i in range(2, n + 1):
#         f[i] = f[i - 1] + f[i - 2]
#     return

dp = [[0, 0] for _ in range(41)]  # N최대 41
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    print(dp[N][0], dp[N][1])

"""
---------------------1출력 재귀(시간초과)--------------------
def fibonacci(n):
    cnt = 0
    if n < 2:
        cnt += 1
        return n
    else:
        cnt += 1
        return fibonacci(n - 1) + fibonacci(n - 2)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    print(f"#{tc} {fibonacci(N)}")
"""
