# 답은 나오지만 시간초과 (Pypy3로도 ㅜ)
import sys
input = sys.stdin.readline
# 재귀 한도 증가
sys.setrecursionlimit(10000)

# 네 방향 전부 살피기
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# bfs로는 너무 복잡해서 풀기 힘듦!
# dfs로 풀 것!!
def dfs(r, c, cnt):
    global alpha_check, result
    # 갈 수 있는 칸 최대 개수와 result 비교해서 최댓값을 result에 넣기
    result = max(cnt, result)

    if result == 26:
        return

    for i in range(4):
    
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위 내에 다음 칸이 있고, 알파벳이 아직 추가되지 않은 경우에만
        if (
            0 <= nr < R
            and 0 <= nc < C
            and board[nr][nc] not in alpha_check
        ):
            alpha_check.append(board[nr][nc])
            dfs(nr, nc, cnt + 1)
            # 백트래킹!
            alpha_check.pop()



R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
# 첫 번째 칸은 기본적으로 항상 성공이므로 그 칸의 문자 미리 입력해줄 것
alpha_check = [board[0][0]]
result = 0

# 첫 번째 칸은 무조건 갈 수 있으므로 한 칸부터 시작해서 다음 칸 살필 것
dfs(0, 0, 1)
print(result)
