import sys
sys.stdin = open('input.txt', 'r')
# 단절점과 단절선
# 단절점 cut vertex    : 해당 정점 제거 시, 정점 포함된 그래프가 2개 이상으로 나눠지는 경우
#                       부모 존재 AND 자식 존재
# 단절선 bridge        : 해당 간선을 제거 시, 간선 포함된 그래프가 2개 이상으로 나눠지는 경우
#                       흠 간선은 없애도 무조건 괜찮은거 아닌감?????흠
# 트리 tree            : 사이클이 존재하지 않고, 모든 정점이 연결된 그래프
#
# N	    # 트리의 정점 개수 (2<= N <= 100,000)
# 	    # 1 ~ n번
# a b	# N-1개의 줄에 걸쳐 주어지는 정보
# 	    # a정점과 b정점이 연결되어 있음, 트리임 보장
# q	    # 질의의 개수, (1<= q <= 100,000)
# t k	# q개의 줄에 걸쳐 주어지는 정보
# 	    # 질의 : t = 1 일 때 k번 정점이 단절점인지? (1<=k<=n)
#               t = 2 일 때 k번 간선이 단절선인지? (1<=k<=n-1)

# 입력받기
N = int(input())    # 노드 개수

tree = [[] for _ in range(N+1)]    # 부모를 인덱스로, 요소는 자식의 위치

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)           # 부모a에 자식b의 내용을 넣기

Q = int(input())    # 질문개수

for _ in range(Q):
    result = 'no'
    t, k = map(int, input().split())

    if t == 1:    # 노드 k를 없애도 트리가 두개 생기는 지? # 질의 검토하기
        # 부모와 자식이 존재해야 한다. 둘 다 필요 AND 조건
        # k 노드를 자식으로 둔 부모 노드의 존재
        # k 노드에 자식이 있는지 검사

        for i in range(1, N + 1):
            if k in tree[i]:  # 부모 노드 존재함
                # print(k, 'yes parents')
                if tree[k]:  # 자식노드 존재함
                    print('yes')

                    continue
                else:   #부모는 있는데 자식이 없음
                    pass

    # 간선 k를 없애도 트리가 두개 생기는 지?
    else:   # 간선을 없애도 단일 노드도 트리로 봐서 무조건 yes
        resuslt = 'yes'
    print(result)



