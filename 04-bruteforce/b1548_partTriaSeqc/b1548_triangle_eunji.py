N = int(input())
arr = list(map(int, input().split()))
arr.sort()

'''
7
2 3 4 1 3 4 5

[1, 2, 3, 3, 4, 4, 5]
'''

# 수열 길이가 3 이상일 때
if N > 2:
    result = 2
    for start in range(N-2):
        end = start + 2
        while end < N:  # 인덱스 범위를 벗어나지 않을 때 까지
            if arr[start] + arr[start+1] > arr[end]:  # 조건 비교
                result = max(result, end-start+1)  # 최대 길이 넣기
                end += 1  # 큰 수 인덱스 이동
            else:
                break  # 조건을 만족하지않으면 중단 -> start 이동
    print(result)
else:  # 수열 길이가 3보다 작으면 바로 출력
    print(N)
