"""
문제 : https://www.acmicpc.net/problem/9934
백준 9934 - 완전 이진 트리리
"""

import sys


def build_tree(arr, level, result, s, e):
    if s > e:
        return

    mid = (s + e) // 2                      #중위순회
    result[level].append(arr[mid])
    # print(f"result는 {result}")

    build_tree(arr, level + 1, result, s, mid - 1) #좌자식
    build_tree(arr, level + 1, result, mid + 1, e) #우자식


K = int(sys.stdin.readline().strip())  # 깊이 K
arr = list(map(int, sys.stdin.readline().strip().split()))

result = [[] for _ in range(K)]

# 방문순서, 현재 깊이 0, 빌딩번호 리스트, 시작, 끝
build_tree(arr, 0, result, 0, len(arr) - 1)

for level in result:
    print(*level)
