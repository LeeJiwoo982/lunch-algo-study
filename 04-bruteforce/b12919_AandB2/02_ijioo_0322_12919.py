def dfs(s, t):
    '''s를 규칙에 맞춰 바꾸면서 t가 될 수 있으면 1, 안되면 0'''
    # 종료 조건
    if len(s) == len(t):
        if s == t:
            return 1
        else:
            return 0
    else:
        pass

    s1 = s + "A"
    if dfs(s1, t) == 1:
        return 1

    s2 = s + "B"
    s2 = s2[::-1]
    if dfs(s2, t) == 1:
        return 1

    return 0
    # # 연산하기
    # for i in range(2):
    #     if i == 0:
    #         s1 = s + "A"
    #         dfs(s1, t)
    #     else:
    #         s2 = s + "B"
    #         s2 = s2[::-1]
    #         dfs(s2, t)

S = input()
T = input()

# 출력 결과로 바꾸기 가능 여부 초기화
# 기본은 안되는 것
result = dfs(S, T)

print(result)