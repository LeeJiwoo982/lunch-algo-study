import sys
sys.stdin = open("input.txt", "r")
# from pprint import pprint
# from collections import deque


def find_position():
    global N, arr, houses, chicken
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                houses.append((i, j))
            if arr[i][j] == 2:
                chicken.append((i, j))


def find_distance(selected_chicken):
    global chicken
    distance = 0
    selected_idx = []
    for i, selected in enumerate(selected_chicken):
        if not selected:
            continue
        selected_idx.append(chicken[i])

    for house_info in houses:
        distance_one = int(21e8)
        house_i, house_j = house_info[0], house_info[1]
        for selected_info in selected_idx:
            chicken_i, chicken_j = selected_info[0], selected_info[1]
            distance_one = min(distance_one, abs(house_i - chicken_i) + abs(house_j - chicken_j))
        distance += distance_one
    return distance


def chicken_distance(chicken_idx, selected, num):
    global N, M, min_distance
    if num == M:
        distance = find_distance(selected)
        min_distance = min(min_distance, distance)
        return
    if chicken_idx >= len(chicken):
        return

    chicken_distance(chicken_idx + 1, selected, num)  # 고르지 않은 경우
    selected[chicken_idx] = 1
    chicken_distance(chicken_idx + 1, selected, num + 1)  # 고른 경우
    selected[chicken_idx] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
houses = []
chicken = []
find_position()

select = [0] * len(chicken)

min_distance = int(21e8)
chicken_distance(0, select, 0)
print(min_distance)





# for i, selected in enumerate(selected_chicken):
#     if not selected:
#         arr1[chicken[i][0]][chicken[i][1]] = 0
# print('arr1')
# pprint(arr1)
# distance = 0
# for house in range(len(houses)):
#     first_i, first_j = houses[house][0], houses[house][1]
#     found = False
#
#     q = deque()
#     q.append((first_i, first_j))
#     visited[first_i][first_j] = 1
#     while q:
#         i, j = q.popleft()
#         print(i, j)
#         for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
#             ni, nj = i + di, j + dj
#             if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]:
#                 continue
#             if arr1[ni][nj] == 2:
#                 print(ni, nj)
#                 found = True
#                 break
#             visited[ni][nj] = visited[i][j] + 1
#             pprint(visited)
#             q.append((ni, nj))
#         if found:
#             distance += visited[i][j]
#             break
#         visited = [[0] * N for _ in range(N)]
#
# for i, selected in enumerate(selected_chicken):
#     if not selected:
#         arr1[chicken[i][0]][chicken[i][1]] = 2





# def find_position():
#     global N, arr, houses, chicken
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 houses.append((i, j))
#             if arr[i][j] == 2:
#                 chicken.append((i, j))
#
#
# def chicken_distance(chicken_idx, num, result):
#     global N, M, min_distance
#     if num == M:
#         min_distance = min(min_distance, result)
#         return
#     if chicken_idx >= len(chicken):
#         return
#
#     if result >= min_distance:
#         return
#
#     chicken_distance(chicken_idx+1, num, result) # 고르지 않은 경우
#     distance = 0
#     for house_info in houses:
#         house_i, house_j = house_info[0], house_info[1]
#         chicken_i, chicken_j = chicken[chicken_idx][0], chicken[chicken_idx][1]
#         distance += abs(house_i - chicken_i) + abs(house_j - chicken_j)
#     chicken_distance(chicken_idx+1, num+1, result+distance) # 고른 경우
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# houses = []
# chicken = []
# find_position()
#
# min_distance = int(21e8)
# chicken_distance(0, 0, 0)
# print(min_distance)
