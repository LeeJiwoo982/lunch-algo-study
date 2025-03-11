'''
트리의 부모 찾기

문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''
# 입력
'''
7
1 6
6 3
3 5
4 1
2 4
4 7

12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
'''
# 출력
'''
4
6
1
3
1
4

1
1
2
3
3
4
4
5
5
6
6
'''

# https://www.acmicpc.net/problem/11725

import sys
sys.stdin = open('input1.txt', 'r')
# sys.stdin = open('input2.txt', 'r')

# 실행시간 단축을 위해 설정할 것
# stdin + deque
from sys import stdin
from collections import deque

# 실행시간 단축을 위해 input()을 다음과 같이 변경
# ⭐같은 작업이 2756ms → 444ms 로 단축됨!!!⭐
def input():
    return stdin.readline().rstrip()

# 부모 저장 위해 bfs 함수 등록
def bfs(s):
    visited = [0] * (N+1)
    
    visited[s] = 1
    q = deque()
    q.append(s)
    while q:
        t = q.popleft()
        # 이동 가능 정점별로 설정
        for line in adj[t]:
            if not visited[line]:
                # 부모 정보 저장
                # 이전 노드의 값을 저장하면 부모의 정보가 저장됨
                visited[line] = t
                q.append(line)

    return visited

N = int(input())

# 간선 정보 저장할 리스트 생성
adj = [[] for _ in range(N+1)]

# 간선 정보 저장
# 순서를 모르니 양방향으로 저장하기
for _ in range(N-1): #100_000
    m1, m2 = map(int, input().split())
    adj[m1].append(m2)
    adj[m2].append(m1)

# 1번 노드를 루트로 하므로 BFS 함수에 1 대입
# 2번 노드부터이므로 range 범위 설정 유의
result = bfs(1)
for i in range(2, N+1): # 100_000
    print(result[i])

# print는 한번만 호출하도록..
# parents = '\n'.join([str(parent) for parent in bfs(1)])
# print(parents)







