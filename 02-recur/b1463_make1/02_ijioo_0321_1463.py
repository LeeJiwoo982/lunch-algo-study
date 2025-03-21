# gpt풀이, 재귀로 풀어달라 요청
def mn_oper(n, memo = None):
    if memo is None:
        memo = {}

    # 기저 사례: 1이 되면 연산 0번
    if n == 1:
        return 0

    # 이미 계산한 값이면 반환
    if n in memo:
        return memo[n]

    # -1 : 모든 경우
    result = mn_oper(n - 1, memo) + 1

    # // 2
    if n % 2 == 0:
        result = min(result, mn_oper(n // 2, memo) + 1)

    # // 3
    if n % 3 == 0:
        result = min(result, mn_oper(n // 3, memo) + 1)

    # 결과 메모이제이션
    memo[n] = result
    print(memo)
    '''
    10
    {2: 1}
    {2: 1, 3: 1}
    {2: 1, 3: 1, 4: 2}
    {2: 1, 3: 1, 4: 2, 5: 3}
    {2: 1, 3: 1, 4: 2, 5: 3, 6: 2}
    {2: 1, 3: 1, 4: 2, 5: 3, 6: 2, 7: 3}
    {2: 1, 3: 1, 4: 2, 5: 3, 6: 2, 7: 3, 8: 3}
    {2: 1, 3: 1, 4: 2, 5: 3, 6: 2, 7: 3, 8: 3, 9: 2}
    {2: 1, 3: 1, 4: 2, 5: 3, 6: 2, 7: 3, 8: 3, 9: 2, 10: 3}
    '''
    return result

n = int(input())
print(mn_oper(n))