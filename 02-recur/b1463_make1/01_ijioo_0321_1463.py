# 1로 만들기
# https://www.acmicpc.net/problem/1463
# 정수 X에 사용할 수 있는 연산
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

# DP문제
# https://jominseoo.tistory.com/98

'''
2 => 1
10 => 3
'''

N = int(input())

dp = [0] * (N+1)

# dp[1] = 0, 1은 연산횟수 0
# dp[i] : i를 만드는 데 필요한 최소 연산 횟수
# bottom-up
for i in range(2, N+1):
    dp[i] = dp[i - 1] + 1   # 1빼기는 모든 경우 가능

    # 2나누기
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3나누기
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
print(dp)
print(dp[N])
# input: 10
# idx: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# dp: [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]
# output: 3

