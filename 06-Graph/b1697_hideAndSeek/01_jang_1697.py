from collections import deque


def bfs(n, k):
    q = deque([n])
    visited = [0] * 100001
    visited[n] = 1

    while q:
        t = q.popleft()  # 현재 위치
        if t == k:  # 동생 위치랑 같으면 리턴
            #print(visited[:20])
            #print(list(range(0, 21)))
            return visited[t] - 1  # 초기값이 1부터 였으니깐 하나 빼주기

        for dx in [1, -1, t]:  # -1 or 1 or 순간이동 2*x -> x+x
            nt = t + dx
            if 0 <= nt <= 100000 and not visited[nt]:
                q.append(nt)
                visited[nt] = visited[t] + 1


N, K = map(int, input().split())  # 수빈, 동생 위치
print(bfs(N, K))
