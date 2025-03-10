# 간식 나누기 행사
# 기다리는 순서가 엉망
# 번호표 순서대로 나눠주기
# 승환=마지막번호
# 1열로 줄서있음 wait
# 맨 앞의 사람만 이동가능
# 번호표 순서대로만 통과가능한 라인 line
# line과 wait줄의 맨 앞 사람 사이에는 한 사람씩 들어갈 수 있는 공간
# 들어올 수 있지만 나가는 건 불가능
# 간식을 받으면 Nice, 아니면 Sad
'''
5
5 4 1 3 2
'''

N = int(input())    #줄 서있는 학생 수

wait = list(map(int, input().split()))  # 엉망으로 엉킨 줄. 요소의 의미는 번호표

stack = []   # wait을 정리하기 위한 stack
order = 1    # 올바른 순서
# 순서 맞는지 확인용 배열
right = []

for p in wait:
    while stack and stack[-1] == order: #스택에 값이 존재하고 맨 위가 기대한 순서라면
        right.append(stack[-1])
        stack.pop()
        order += 1

    if p == order:  #사람이 올바른 순서면
        right.append(p)
        order += 1
    else:   # 올바른 순서의 사람이 아니면 스택에 대기
        stack.append(p)

while stack and stack[-1] == order: # 스택에 남은 사람 순서대로 빵을 먹는지
    right.append(stack[-1])
    stack.pop()
    order += 1
# if not stack:
#     print('Nice')
# else:print('Sad')

print(right)
print('Nice' if not stack else 'Sad')
