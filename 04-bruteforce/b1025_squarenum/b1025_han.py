# 제곱수 찾기
# https://www.acmicpc.net/problem/1025


import sys
input = sys.stdin.readline

N, M = map(int,input().split())
board = [list(input().strip()) for _ in range(N)]
# 일단 값이 없다고 가정 후 탐색 시작
answer = -1

# 제곱수 확인용 함수
# math보단 직접 쉽게 구할 수 있는 방법 쓰는 것도 추천
def sqr(num):
    num = int(num)
    return int(num ** 0.5) ** 2 == num


for r in range(N): #시작 행
    for c in range(M): # 시작 열
        for dr in range(-N,N): # 행의 등차
            for dc in range(-M,M): # 열의 등차
                number = ""
                nr,nc = r,c
                if dr == 0 and dc == 0:
                    continue
                # 한 숫자씩 더해가며 각각 확인해야 하므로 while문 이용
                while 0 <= nr < N and 0 <= nc < M:
                    number += board[nr][nc]
                    # 제곱수가 맞다면 최댓값으로 answer 변환
                    if sqr(number):
                        answer = max(answer,int(number))
                    # 행, 열의 등차수열에 맞추어 다음 숫자 합치고 확인
                    nr += dr
                    nc += dc
print(answer)