import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def mix_card(K, i, arr):    # i = 섞은 횟수
    if i == K+1:
        return arr
    
    L = len(arr)
    arr = mix_card(K, i+1, arr[L - 2**(K-i):])+ arr[:L - 2**(K-i)]
    return arr

N = int(input())
original = list(range(1, N+1))
cards = [*map(int, input().split())]

found = False
K1 = 1
while 2 ** K1 < N and not found:
    result1 = mix_card(K1, 0, original)
    
    K2 = 1
    while 2 ** K2 < N:
        result2 = mix_card(K2, 0, result1)

        if result2 == cards:
            print(K1, K2)
            found = True
            break
        K2 += 1

    K1 += 1

