from collections import deque
import sys

input = sys.stdin.readline  # 빠른 입력을 위해 추가

# 리프노드를 찾아서 개수를 반환하는 함수
def find_leaf(tree):
    visited = [0] * (N+1)
    ct = 0  # 리프노드 개수 저장할 변수
    q = deque([1])
    visited[1] = 1

    while q:
        check = True  # 리프노드인지 체크할 변수
        t = q.popleft()
        for w in tree[t]:
            if visited[w] == 0:  # 간 적이 없는 곳이 있다면 리프노드가 아님
                q.append(w)
                visited[w] = 1
                check = False

        if check:  # 리프노드 세기
            ct += 1

    return ct

N, W = map(int, input().split())  # 노드의 수, 고인 물의 양
tree = [[] for _ in range(N+1)]  # [[], [2, 3], [1], [5, 4, 1], [3], [3]]

for _ in range(N-1):
    U, V = map(int, input().split())  # 연결된 두 노드가 들어옴
    tree[U].append(V)  # 무방향으로 트리에 넣어놓기
    tree[V].append(U)

'''
각 정점에 쌓인 물의 양(0보다는 큰)들의 평균을 구해야함
-> 맨 위 정점은 다 0일 것임. 물이 남아 있는 노드는 리프노드들이다. 
-> (W / 리프노드개수) 가 정답이다.
'''

num = find_leaf(tree)  # 리프 노드 개수 저장

if num == 0:  # 리프 노드가 없으면 W 그대로 출력
    print(W)
else:
    print(W / num)  # 리프 노드 개수로 나눈 값 -> 평균

'''
5 20
5 3
3 4
2 1
1 3
'''
