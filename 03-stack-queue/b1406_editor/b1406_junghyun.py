import sys
# sys.stdin = open("input1.txt", "r")
# sys.stdin = open("input2.txt", "r")
# sys.stdin = open("input3.txt", "r")

arr = list(input())
M = int(input())
cursor = len(arr)
for _ in range(M):
    mode = list(input().split())
    if mode[0] == 'L':
        if cursor > 0:
            cursor -= 1
    if mode[0] == 'D':
        if cursor < len(arr):
            cursor+=1
    if mode[0] == 'B':
        if cursor > 0:
            arr.remove(arr[cursor - 1])
            cursor -= 1
    if mode[0] == 'P':
        arr.insert(cursor, mode[1])
        cursor += 1

print(''.join(arr))