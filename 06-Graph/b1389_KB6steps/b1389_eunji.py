def bfs(i, adj):
    visited = [-1] * (N+1)  # 방문배열. 거리체크를 위해 -1로 저장(-1이면 방문 x)
    visited[i] = 0  # 자기 자신까지의 거리는 0
    q = [i]  # q에 넣어놓기

    while q:  # 갈 곳이 있을 때까지
        t = q.pop(0)
        for f in adj[t]:  # 친구 찾아가기
            if visited[f] == -1:  # 방문하지않았다면
                visited[f] = visited[t] + 1  # 이전 거리 + 1 해서 거리 저장
                q.append(f)  # 큐에 친구 넣기

    return sum(visited[1:])  # 처음 인덱스(=-1) 빼고 거리의 합 반환

N, M = map(int, input().split())  # 사람 수, 관계 수(간선)
adj = [[] for _ in range(N+1)]  # 인접리스트 생성, 무방향

for _ in range(M):  # M개의 간선
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

bacon = []  # 각 사람의 케빈 베이컨 수 저장
for i in range(1, N+1):
    bacon.append((bfs(i, adj), i))  # 번호랑 같이 저장

bacon.sort()
print(bacon[0][1])  # 베이컨 오름차순 정렬하고 번호를 출력

'''
5 5
1 3
1 4
4 5
4 3
3 2
'''
