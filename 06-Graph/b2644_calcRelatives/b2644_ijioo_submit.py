from collections import deque
# import sys
# sys.stdin = open('input.txt', 'r')
# 촌수계산
def evaluate_relative(X, Y, n):  # 현재사람번호, 인간수
    '''bfs로 최단 촌수 구하기'''
    visited = [False] * (n + 1)
    cnt = 0
    q = deque()
    q.append((X, cnt))  # 관계의 시작 사람 번호, 촌수

    while q:  # q가 있을때
        fam, cnt = q.popleft()  # 가족과 촌수

        if fam == Y:  # 종료조건1:목표하는 가족을 찾을때
            return cnt

        if not visited[fam]:  # 검사안한 가족일때
            visited[fam] = True  # 검사했음 기록
            for f in relation[fam]:
                # 인접가족 순회
                if not visited[f]:  # 인접가족이 검사안한 경우에만
                    q.append((f, cnt + 1))
    return -1

n = int(input())  # 전체사람 수
X, Y = map(int, input().split())  # 촌수계산해야 하는 사람
m = int(input())  # 부모 자식 관계의 개수

relation = [[] for _ in range(n + 1)]  # 관계정보 입력 2차원 리스트
for i in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

result = evaluate_relative(X, Y, n)
print(result)