from collections import deque
import sys
sys.stdin = open("input.txt", "r")


def bfs(r, c):
    global group_num, room_info, visited, arr, N, M

    q = deque()
    q.append((r, c))

    visited[r][c] = 1
    area = 1

    group = []
    group.append((r, c))

    while q:
        tr, tc = q.popleft()

        for i in range(4):
            if not(arr[tr][tc] & 2**i):
                nr = tr + dr[i]
                nc = tc + dc[i]
                if 0<=nr<M and 0<=nc<N and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    area+=1
                    q.append((nr, nc))
                    group.append((nr, nc))

    for i, j in group:
        room_info[i][j][0] = group_num
        room_info[i][j][1] = area
        
    group_num+=1
    return area



# 알고리즘 시작
N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(M)]
# print(arr)
visited = [[0]*N for _ in range(M)] # 방문 체크
room_info=[[[0]*2 for _ in range(N)] for _ in range(M)]
# 해당 인덱스에 룸의 번호, 총 넓이 저장할 리스트

# print(room_info)

dr = [0, -1, 0, 1] # 서 북 동 남 의 순서로
dc = [-1, 0, 1, 0] # 2**(idx)가 1서, 2북, 4동, 8남
# 비트 연산자로 풀었음.

group_num=0 # 방의 개수 변수
# print(bfs(0, 0))
max_area = 0 # 최대값 변수

for i in range(M):
    for j in range(N):
        if not visited[i][j]: # 방문하지 않은 칸만 체크
            max_area = max(max_area, bfs(i, j)) # 최대값 갱신

max_del_wall = 0
for r in range(M):
    for c in range(N):
        for d in range(4):
            if arr[r][c] & 2**d:
                nr, nc = r+dr[d], c+dc[d]
                if 0<=nr<M and 0<=nc<N:
                    if room_info[r][c][0] != room_info[nr][nc][0]:
                        max_del_wall = max(max_del_wall, room_info[r][c][1] + room_info[nr][nc][1])
print(group_num)
print(max_area)
print(max_del_wall)


##### 참고 문서 #####
# 문제 링크: https://www.acmicpc.net/problem/2234
# https://velog.io/@mimmimmu/12%EC%A3%BC%EC%B0%A8-%EB%B0%B1%EC%A4%80-2234%EB%B2%88-%EC%84%B1%EA%B3%BD-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://yabmoons.tistory.com/59


# group_num 을 어떻게 추가해줘야할까에 대한 시행착오
# 방 개수와 최대 넓이까지만 구했음

# from collections import deque
# import sys
# sys.stdin = open("input1.txt", "r")
#
# def bfs(r, c):
#     global group_num, visited, arr, N, M
#
#     if 0<=r<M and 0<=c<N and not visited[r][c]:
#         group_num+=1
#
#     q = deque()
#     q.append((r, c))
#     visited[r][c] = 1
#     area = 1
#
#     while q:
#         tr, tc = q.popleft()
#
#         for i in range(4):
#             if not(arr[tr][tc] & 2**i):
#                 nr = tr + dr[i]
#                 nc = tc + dc[i]
#                 if 0<=nr<M and 0<=nc<N and not visited[nr][nc]:
#                     visited[nr][nc] = 1
#                     area+=1
#                     q.append((nr, nc))
#     return area
#
#
# N, M = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for _ in range(M)]
# # print(arr)
# visited = [[0]*N for _ in range(M)]
#
# dr = [0, -1, 0, 1] # 서 북 동 남 의 순서로
# dc = [-1, 0, 1, 0] # 2**(idx)가 1서, 2북, 4동, 8남
#
# group_num=0
# # print(bfs(0, 0))
# max_area = 0
# for i in range(M):
#     for j in range(N):
#         max_area = max(max_area, bfs(i, j))
# print(group_num, max_area)