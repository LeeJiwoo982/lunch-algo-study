import sys
sys.stdin = open('input.txt', 'r')
# 단절점과 단절선
# 단절점 cut vertex    : 해당 정점 제거 시, 정점 포함된 그래프가 2개 이상으로 나눠지는 경우
# 단절선 bridge        : 해당 간선을 제거 시, 간선 포함된 그래프가 2개 이상으로 나눠지는 경우
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
N = int(input())
tree = [list(map(int, input().split())) for _ in range(N-1)]    # N-1줄
Q = int(input())
for _ in range(Q):
    t, k = map(int, input().split())
    if t == 1:

        pass
    else:
        pass
