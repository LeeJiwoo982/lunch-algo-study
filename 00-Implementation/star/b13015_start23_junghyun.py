# from pprint import pprint
# 1. 출력 꼴 분석하기
# N = int(input())
# print('*'*N + ' '*(2*N-3) + '*'*N)
# for i in range(1, N-1):
#     print(' '*(i) + '*' + ' '*(N-2) + '*' + ' '*(2*(N-i)-3) + '*' +' '*(N-2) + '*')
# print(' '*(N-1)+'*' + ' '*(N-2) + '*' + ' '*(N-2) + '*')
# for i in range(N-2, 0, -1):
#     print(' '*(i) + '*' + ' '*(N-2) + '*' + ' '*(2*(N-i)-3) + '*' +' '*(N-2) + '*')
# print('*'*N + ' '*(2*N-3) + '*'*N)

# 2. arr로 만들어버리기
N = int(input())
arr = [[' ']*(4*N-3) for _ in range(2*N-1)]
# print(arr)
for i in range(2*N-1):
    if i==0 or i==2*N-2:
        for j in range(N):
            arr[i][j]='*'
            arr[i][4*N-4-j]='*'
    elif i==N-1:
        arr[i][N-1] = '*'
        arr[i][2*(N-1)] = '*'
        arr[i][3*(N-1)] = '*'
    else:
        if i<N:
            arr[i][i] = '*'
            arr[i][N+i-1] = '*'
            arr[i][4*N-4 -i] = '*'
            arr[i][4*N-4-(N+i-1)] = '*'
        else:
            
            arr[i][N-i+(N-2)] = '*'
            arr[i][N-i+(N-2)+(N-2)+1] = '*'
            arr[i][N+i-1] = '*'
            arr[i][N+i-1+(N-2)+1] = '*'
            pass
    print(''.join(arr[i]).rstrip())
# pprint(arr)
# 출력 형식이 잘 못 되었다고 뜬다...
# rstrip으로 오른쪽 공백을 없애주니 맞았습니다 받음


# 3. 재귀꼴?이 될까?