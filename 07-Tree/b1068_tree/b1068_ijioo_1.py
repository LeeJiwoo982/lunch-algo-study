# import sys
# sys.stdin= open('input_ijioo.txt', 'r')

# 리프노드 ; 자식의 개수 0
# 트리가 주어짐
# 노드 하나 지울 것. 이때 남은 트리의 리프 노드 개수 구하기
# 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거

N = int(input())    # 노드의 개수
child = [[] for _ in range(N)]   # 노드가 0번부터 임
parents = list(map(int, input().split()))
for i, v in enumerate(parents):
    if v == -1:
        pass
    else:
        child[v].append(i)

input()
print(child)