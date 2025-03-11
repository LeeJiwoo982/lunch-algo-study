from collections import deque

N, K = [*map(int, input().split())]
arr = deque(range(1, N+1))
result = []
i = 0
while arr:
    arr.rotate(-(K-1))
    result.append(arr.popleft())
print(f"<{', '.join(map(str, result))}>")

''' 모드 연산 사용
---------------------------------------------------------------
N, K = [*map(int, input().split())]
arr = [i for i in range(1, N+1)]
result = []
i = 0
while arr:
    i = (i+K-1) % len(arr)
    print(i, arr)
    print(f'길이 : {len(arr)}')
    print()
    a = arr.pop(i)
    result.append(a)
print(f"<{', '.join(map(str, result))}>")
'''


# 아래와 같이 구현하지 않도록 주의!
'''
while arr:
    i = i + K - 1
    a = arr.pop(i % len(arr))
    result.append(a)
'''
# i를 직접 증가(i + K - 1)시킨 후 mod 연산(% len(arr))을 수행
# i값에 mod 연산이 반영되지 못함
# 다음 순번에서 i 값이 꼬임.


