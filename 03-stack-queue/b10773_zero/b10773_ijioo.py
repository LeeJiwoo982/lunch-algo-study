import sys
sys.stdin = open('input2.txt', 'r')

K = int(input())

# K개의 정수
# 0이면 마지막 수 지우기, 아니면 해당 수를 쓰기
plus = []   # 더할 후보 리스트

for _ in range(K):
    k = int(input())
    if k == 0:  #0이면 지우기
        plus.pop()  #마지막 수를 지운다.
    else:
        plus.append(k)


print(sum(plus))
