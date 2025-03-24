# 12919 a와 b
# https://www.acmicpc.net/problem/12919
# 문자열 뒤에 A추가
# 문자열 뒤에 B 추가, 문자열 뒤집기

def reverse_dfs(t):
    '''결과에서부터 지워가며 S만들기'''
    # 둘의 길이가 같을 때
    # 그 둘이 같다면 1, 아니면 0 출력됨
    # 파이썬에서 False는 0으로, True는 1로 판정
    if len(t) == len(S):
        return int(t == S)

    # 결과문자가 마지막이 A이면 슬라이싱으로 재귀
    # 둘이 만족하면 1
    if t[-1] == 'A' and reverse_dfs(t[:-1]):
        return 1    # 바로 성공하면 바로 리턴해버림

    # t의 첫값이 B, 그 t: 1~ -1까지, 그걸 뒤집기 한게 맞으면 1
    if t[0] == 'B' and reverse_dfs(t[1:][::-1]):
        return 1        # 바로 성공하면 그만 찾아도 됨

    # 다 안되면 0
    return 0        # 다른 길을 찾아야 함

S = input()
T = input()
print(reverse_dfs(T))

# S에서 T로 가는 경우의 수가 너무 많음
# 거꾸로 줄여가며 생각하는 게 효율적

