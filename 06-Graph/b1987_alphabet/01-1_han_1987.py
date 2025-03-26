import sys

# 빠른 입력을 위한 세팅
input = sys.stdin.readline

# 재귀 깊이 제한 해제 (DFS 깊이 방지용)
sys.setrecursionlimit(10000)

# 상하좌우 이동을 위한 방향 배열
dr = [1, 0, -1, 0]  # 아래, 오른쪽, 위, 왼쪽
dc = [0, 1, 0, -1]

def dfs(r, c, cnt):
    """현재 좌표 (r, c)에서 cnt칸을 밟은 상태로 DFS 수행"""
    global result

    # 최대 경로 길이 갱신
    result = max(result, cnt)

    # 알파벳 26개 전부 방문했다면 더 볼 것도 없이 종료
    if result == 26:
        return

    # 4방향 모두 탐색
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 보드 범위 내에 있는지 확인
        if 0 <= nr < R and 0 <= nc < C:

          '''
          범위 검사!!! → 격자 안에 있는지 확인
          ord()는 문자를 아스키코드로 바꾸고, 'A'를 빼서 0~25로 매핑합니다
          예: 'A' → 0, 'B' → 1 ... 'Z' → 25
          '''
            # 다음 칸의 알파벳을 인덱스로 변환 (0 ~ 25)
            idx = ord(board[nr][nc]) - ord('A')

            # 해당 알파벳을 아직 밟지 않았다면
            if not visited[idx]:
                visited[idx] = True          # 방문 처리
                dfs(nr, nc, cnt + 1)         # 재귀 호출 (한 칸 더 진행)
                visited[idx] = False         # 백트래킹 (방문 해제)

# 행(R), 열(C) 입력
R, C = map(int, input().split())

# 보드 정보 입력 (rstrip으로 개행 문자 제거)
board = [list(input().rstrip()) for _ in range(R)]

# 알파벳 방문 여부를 나타내는 배열 (A~Z → 0~25)
visited = [False] * 26

# 시작 위치 (0,0)의 알파벳은 처음부터 밟았으므로 True 처리
visited[ord(board[0][0]) - ord('A')] = True

# 최댓값 초기화
result = 0

# DFS 시작 (시작 좌표, 시작 카운트 1)
dfs(0, 0, 1)

# 결과 출력
print(result)
