import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().rstrip())
# arr = [(0, 0) for _ in range(N)]
# # print(arr)
# for i in range(N):
#     arr[i] = tuple(map(int, input().split()))
# # print(arr)
# # # x[1]로 먼저 sort, x[1]이 같으면 x[0]으로 sort 됨
# arr.sort(key=lambda x: (x[1], x[0])) 
# # print(arr)

# 다른 방법: arr를 저장할 때부터 end시간, start 시간으로 저장한다 => sort 하면?
# lambda에 x[0]을 추가하지 않아도 다음 시간까지 보고 정렬한다
arr = [(0, 0) for _ in range(N)]
for i in range(N):
    start, end = map(int, input().split())
    arr[i] = (end, start)
arr.sort()
print(arr)

s, e = arr[0]
cnt = 1
for i in range(1, N):
    ns, ne = arr[i]
    if ns >= e:
        cnt+=1
        s, e = ns, ne
print(cnt)