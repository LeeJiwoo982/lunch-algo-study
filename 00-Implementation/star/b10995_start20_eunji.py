N = int(input())
for i in range(N):
    for j in range(N*2):
        if (i + j) % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()