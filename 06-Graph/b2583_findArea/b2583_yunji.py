from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x, paper):
    q = deque()
    area = 0
    q.append((y, x))
    paper[y][x] = 2
    while q:
        cy, cx = q.popleft()
        area += 1
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < M and 0 <= nx < N:
                if paper[ny][nx] == 0:
                    paper[ny][nx] = 2
                    q.append((ny, nx))
    return area


M, N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]

paper = [[0] * N for _ in range(M)]


for i in range(K):
    x1, y1, x2, y2 = arr[i]
    for x in range(x1, x2):
        for y in range(y1, y2):
            paper[y][x] = 1

area_count = 0
areas = []
for y in range(M):
    for x in range(N):
        if paper[y][x] == 0:
            area_count += 1
            areas.append(bfs(y, x, paper))


print(area_count)
print(*sorted(areas))
