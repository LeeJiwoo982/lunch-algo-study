from collections import defaultdict
import sys
input = sys.stdin.readline

graph = defaultdict(list)
N = int(input())

#간선 입력받기
for _ in range(N-1) :
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 문제 입력받아서 답 출력
for _ in range(int(input())) :
    t, k = map(int, input().split())
    if t == 1 :
        print("yes" if 1 < len(graph[k]) else "no") #간선 개수로 단절점인지 판단
    elif t == 2 :
        print("yes") #모든 간선이 단절선