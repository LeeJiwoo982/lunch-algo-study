# 입력받기
N = int(input())    # 노드 개수

edges = [list(map(int, input().split())) for _ in range(N-1)]   # 간선 정보
#부모 확인 배열
is_parents = [0]*(N+1)
is_child = [[] for _ in range(N+1)]
for p, c in edges:
    is_parents[c] += 1
    is_child[p].append(c)

Q = int(input())    #질의개수
result = [0]*Q

for q in range(Q):
    t, k = map(int, input().split())

    if t == 1:
        if is_parents[k] == 0 and is_child[k]:
            result[q] = 'no'
        else:
            result[q] = 'yes'
    else: result[q] = 'yes'
print('\n'.join(result))