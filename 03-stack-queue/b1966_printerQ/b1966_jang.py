from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())  # 문서의 개수, 찾을 문서
    imp = list(map(int, input().split()))  # 중요도

    q = deque(enumerate(imp))  # 인덱스, 중요도
    # deque([(0, 1), (1, 2), (2, 3), (3, 4)])

    ct = 0  # 몇 번째로 빼냈는지 저장할 변수

    while q:
        num, imp = q.popleft()  # 큐에서 처음꺼 빼오기

        check = True  # 지금 문서가 중요도가 제일 높은지 확인
        for i in range(len(q)):  # 현재 큐를 돌면서 확인
            if imp < q[i][1]:
                check = False  # 지금것보다 높은게 있으면 False
                break

        if check:  # True라면 현재 중요도가 제일 높다는 것 -> 꺼낸 상태로 두기
            ct += 1  # 몇번째로 꺼냈는지 확인하기 위해
            if num == M:  # 찾으려는 문서와 번호가 같다면 멈추기
                break
        else:  # False라면 다시 큐에 넣기
            q.append((num, imp))

    print(ct)  # 몇 번째로 꺼냈는지 출력
