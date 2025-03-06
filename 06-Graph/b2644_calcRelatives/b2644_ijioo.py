# 촌수계산
n = int(input())    #전체사람 수
X, Y = map(int, input().split())    #촌수계산해야 하는 사람
m = int(input())    #부모 자식 관계의 개수

relation = [[] for _ in range(n+1)] #관계정보 입력 2차원 리스트
for i in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

# print(relation) 입력값 들어갔는지 확인. 양방향

visited = [False]*(n+1)
visited[0] = True

print(visited)
stack = []
cnt = 0 #촌수저장
x = X

while True:
    # 종료조건1: 촌수계산할 대상이 되면
    if x == Y:
        print(cnt)
        break
    # 종료조건2: 더 이상 이동할 수 없을 때 (혈연관계가 아닌 경우)
    if not stack and all(visited[w] for w in relation[x]):
        print(-1)  # 촌수 계산이 불가능함을 의미
        break

    if not visited[x]:  #방문안한 정점이면
        visited[x] = True
        cnt += 1    #촌수 저장

    for w in relation[x]:   #방문안한 정점 순회
        if not visited[w]:
            stack.append(x)
            x = w
            break
    else:   #갈 곳이 없다면
        if stack:   #스택에 남아있으면
            x = stack.pop()
            cnt = 0
        else:
            break