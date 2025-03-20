from sys import stdin
import sys

def input():
    return stdin.readline().rstrip()
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 (1000번을 넘으면 오류남)

# 그냥 for문으로 M~N 확인
# M, N = map(int, input().split())
# for i in range(M, N + 1):
#     if i == 1:
#         continue
#     for j in range(2, int(i ** (1/2)) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# 재귀로 풀기 (비추천)
def check_num(num):
    if num > N:
        return

    for i in range(2, int(num**(1/2)) + 1):  # 참고(에라토스테네스의 체)
        if num % i == 0:
            break
    else:
        print(num)

    check_num(num + 1)

M, N = map(int, input().split())
if M == 1:
    M = 2
if N > 1:
    check_num(M)