N = int(input())  # 노드 개수

# 트리 저장
tree = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

Q = int(input())  # 질의 개수

result = []
for _ in range(Q):
    t, k = map(int, input().split())

    if t == 1:  # 단절점 확인
        if len(tree[k]) > 1:  # 연결된 간선이 2개 이상이면 단절점
            result.append("yes")
        else:
            result.append("no")
    else:  # 단절선 확인
        result.append("yes")  # 트리에서 모든 간선은 단절선

# 출력
print("\n".join(result))


#이 문제는 결국 간선의 개수를 물어보는 것이라
# 트리 정보를 입력 받을 때 쌍방향이라 생각하고 받았어야 함.
# 단순히 루트이고 리프이면 단절점이 아닌 것이 아님
#