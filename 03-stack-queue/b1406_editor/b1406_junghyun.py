import sys

sys.stdin = open("input1.txt", "r")
# sys.stdin = open("input2.txt", "r")
# sys.stdin = open("input3.txt", "r")

# 1406 : https://www.acmicpc.net/problem/1406

# 참고: https://seongonion.tistory.com/53
# 참고: https://velog.io/@tkdduf727/%EB%B0%B1%EC%A4%80-%EA%B4%84%ED%98%B8-1406%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0

# 시간 초과가 난다.
# 시간 초과가 나는 이유: insert
# insert에서 위치를 지정해주면서 해당 위치만큼 for문을 돌게 된다.
#
arr = list(input())
M = int(input())
cursor = len(arr)
for _ in range(M):
    mode = list(input().split())
    if mode[0] == 'L':
        if cursor > 0:
            cursor -= 1
    elif mode[0] == 'D':
        if cursor < len(arr):
            cursor+=1
    elif mode[0] == 'B':
        if cursor > 0:
            arr.remove(arr[cursor - 1])
            cursor -= 1
    else:
        arr.insert(cursor, mode[1])
        cursor += 1

print(''.join(arr))


# arr1과 arr2를 만들고,
# cursor 앞은 arr1에, cursor 뒤는 arr2에 넣어주었다
# 그러나 여전히 시간초과가 남

# arr1 = list(input().rsplit())
# M = int(input())
# arr2 = []
#
# for _ in range(M):
#     mode = list(input().split())
#     if mode[0] == 'L':
#         if arr1:
#             arr2.append(arr1.pop())
#     elif mode[0] == 'D':
#         if arr2:
#             arr1.append(arr2.pop())
#     elif mode[0] == 'B':
#         if arr1:
#             arr1.pop()
#     else:
#         arr1.append(mode[1])
# arr1.extend(reversed(arr2))
# print(''.join(arr1))


# sys.stdin.readline()으로 바꿔서 다시 풂
# rstrip이 필수다!!!!!!!!! '/n'이 들어가 있는 경우가 있음!!!

import sys

left = list(sys.stdin.readline().rstrip())
# print(left)
right = []

for _ in range(int(sys.stdin.readline())):
    mode = list(sys.stdin.readline().split())
    if mode[0] == 'L':
        if left:
            right.append(left.pop())
    elif mode[0] == 'D':
        if right:
            left.append(right.pop())
    elif mode[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(mode[1])
    # print(mode, left, right)
# arr_left.extend(reversed(arr_right))
print(''.join(left + list(reversed(right))))

import sys

stack_l = list(input())
stack_r = []
n = int(input())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "L" and stack_l:
        stack_r.append(stack_l.pop())
    elif command[0] == "D" and stack_r:
        stack_l.append(stack_r.pop())
    elif command[0] == "B" and stack_l:
        stack_l.pop()
    elif command[0] == "P":
        stack_l.append(command[1])

print("".join(stack_l + list(reversed(stack_r))))
