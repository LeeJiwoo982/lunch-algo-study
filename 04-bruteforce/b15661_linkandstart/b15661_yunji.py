N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N
ans = float("inf")

def team():
    global ans

    start, link = 0, 0

    for i in range(N):
        for j in range(i+1, N):
            if visited[i] and visited[j]: # 스타트 팀
                start += S[i][j] + S[j][i]
            elif not visited[i] and not visited[j]: # 링크 팀
                link += S[i][j] + S[j][i]
    
    ans = min(ans, abs(start-link))
    return

def score(i):
    if i == N: # n명 모두 팀이 정해졌을 때
        team() # 시너지 계산할거야야
        return
    
    visited[i] = 1
    score(i+1)
    visited[i] = 0
    score(i+1)

score(0)
print(ans)