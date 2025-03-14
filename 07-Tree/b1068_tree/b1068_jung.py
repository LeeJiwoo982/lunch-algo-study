import sys
sys.stdin= open('input.txt', 'r')

"""
백준 링크: https://www.acmicpc.net/problem/1068

1. 인접 행렬로 풀었음 (맞았습니다)
- check[출발 인덱스][도착 인덱스] == 1이면 갈 수 있음, 0이면 갈 수 없음 으로 저장
- check[부모 인덱스][지우려는 인덱스] = 0으로 만들어버리고
- 입력이 -1인 루트부터 BFS/DFS 돌리면서
- 자식이 없으면 cnt+=1 (더이상 갈 수 있는 곳이 없으면 cnt+=1)

2. 이진트리 순회 방식 (틀렸습니다)
- 트리가 이진트리라면 left, right로 돌수있을듯~!
- 틀렸습니다가 떴다. 이진트리가 아닐수도 있나보다

3. chatGPT에게 풀어보라고 해서 나온 코드
- return 0 을 활용해서 좀더 시간이 줄었을 것 같다.
"""

# 1. 인접 행렬로 푼 내용
from collections import deque

def bfs():
    global cnt

    # 루트를 삭제했으면 bfs 스킵
    if skp == True:
        return

    q = deque()
    q.append(si)
    while q:
        idx = q.popleft()

        # 지금 idx에서 갈 수 있는 자식 노드 a에 append
        a = deque()
        for n in range(N):
            if check[idx][n] == 1:
                a.append(n)

        # 자식이 없으면 cnt+1
        if len(a) == 0:
            cnt += 1

        # q에 append
        for n in a:
            q.append(n)

        # q.append(n for n in a)
        # 이건 deque에서는 안 먹히는지 렉이 걸린다.
    pass


# 입력 받기
N = int(input())
tree = list(map(int, input().split()))
del_idx = int(input())

check = [[0] * N for _ in range(N)] # 인접 배열

for i in range(N):
    if tree[i] == -1: # 루트 체크
        si = i
    else:
        check[tree[i]][i] = 1

# 지우려는 노드가 루트 노드면 스킵
skp = False
if del_idx == si:
    skp = True

# 지우려는 인덱스의 부모노드에서 지우려는 인덱스로 가는 길 차단
check[tree[del_idx]][del_idx] = 0

cnt = 0
bfs()

print(cnt)



# 2. 트리 순회로 풀기 ( 틀 림 )

# def traversal(T):
#     global cnt, skp
#     if skp:
#         return
#     if left[T] != -1:
#         traversal(left[T])
#         if right[T] != -1:
#             traversal(right[T])
#     else:
#         cnt += 1
#     # print('T', T, '/', 'left', left, '/', 'right', right, '/', 'cnt', cnt)
#
#
#
# N = int(input())
# tree = list(map(int, input().split()))
# del_idx = int(input())
#
# left = [-1]*N
# right = [-1]*N
#
# skp = False
#
# for i, parent in enumerate(tree):
#     if parent == -1:
#         start = i
#         if del_idx == start:
#             skp = True
#     elif left[parent]!=-1:
#         right[parent]=i
#     else:
#         left[parent]=i
#
# if left[tree[del_idx]] == del_idx:
#     left[tree[del_idx]] = right[tree[del_idx]]
#     right[tree[del_idx]] = -1
# elif right[tree[del_idx]] == del_idx:
#     right[tree[del_idx]] = -1
#
# # print(left, right)
#
# cnt = 0
# traversal(start)
# print(cnt)




# 3. chatGPT
# - 틀려서 조금 손봤다.
# - ? 뭔가 손보기 힘들다. 포기

# def count_leaf_nodes(N, tree, del_idx):
#     # 부모 노드가 -1인 것은 루트 노드임
#     # 부모-자식 관계를 연결할 배열을 만들기
#     children = [[] for _ in range(N)]
#
#     # 트리에서 부모-자식 관계를 정의
#     for i in range(N):
#         if tree[i] != -1:
#             children[tree[i]].append(i)
#         else:
#             start = i
#
#     # 삭제할 노드가 루트일 경우, 더 이상 트리가 없으므로 0을 반환
#     if del_idx == start:
#         return 0
#
#     # 삭제된 노드를 트리에서 제거하기 위해 부모와의 연결 끊기
#     for i in range(N):
#         if tree[i] == del_idx:
#             tree[i] = -1  # 삭제된 노드는 부모가 -1로 설정되므로 자식에서 제외됨
#
#     # 리프 노드를 계산하기 위한 변수
#     leaf_count = 0
#
#     # 모든 노드를 탐색하면서 자식이 없으면 리프 노드로 카운트
#     for i in range(N):
#         if i != del_idx:  # 삭제된 노드는 제외
#             if len(children[i]) == 0:  # 자식이 없으면 리프 노드
#                 leaf_count += 1
#
#     return leaf_count
#
#
# # 입력 받기
# N = int(input())  # 노드의 개수
# tree = list(map(int, input().split()))  # 부모 노드를 나타내는 배열
# del_idx = int(input())  # 삭제할 노드의 인덱스
#
# # 결과 출력
# print(count_leaf_nodes(N, tree, del_idx))
