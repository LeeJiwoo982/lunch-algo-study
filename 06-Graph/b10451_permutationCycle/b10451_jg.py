# 순열 사이클 다국어
'''
1부터 N까지 정수 N개로 이루어진 순열을 나타내는 방법은 여러 가지가 있다. 예를 들어, 8개의 수로 이루어진 순열 (3, 2, 7, 8, 1, 4, 5, 6)을 배열을 이용해 표현하면  
\(\begin{pmatrix} 1 & 2 &3&4&5&6&7&8 \\  3& 2&7&8&1&4&5&6 \end{pmatrix}\) 와 같다. 또는, Figure 1과 같이 방향 그래프로 나타낼 수도 있다.
순열을 배열을 이용해  
\(\begin{pmatrix} 1 & \dots & i & \dots &n \\  \pi_1& \dots& \pi_i & \dots & \pi_n \end{pmatrix}\) 로 나타냈다면, i에서 πi로 간선을 이어 그래프로 만들 수 있다.
Figure 1에 나와있는 것 처럼, 순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다. 이러한 사이클을 "순열 사이클" 이라고 한다.
N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.

출력
각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.
'''
# 입력
'''
2
8
3 2 7 8 1 4 5 6
10
2 1 3 4 5 6 7 9 10 8
'''
# 출력
'''
3
7
'''

import sys
sys.stdin = open('input.txt', 'r')
# GPT가 열일해줬습니다...
# 순열 사이클 : 어떤 순열에서 연결된 원소들이 하나의 닫힌 루프를 이루는 것

def dfs(arr, N):
    # 방문 표시할 배열 생성
    visited = [0]*(N+1)

    # 순열 사이클 수 기록 변수
    cnt = 0

    # 인덱스 숫자 맞춰줬으므로 1부터 시작
    for i in range(1, N+1):
        # 처음 방문하는 숫자일 때
        if not visited[i]:
            cnt += 1

            ni = i
            # 사이클이 끝날 때까지 탐색
            while not visited[ni]:
                visited[ni] = 1
                ni = arr[ni]
    return cnt

# 테스트케이스 개수 입력
T = int(input())

for tc in range(T):
    N = int(input())

    # 인덱스 숫자 맞춤용 0 추가
    arr = [0] + list(map(int, input().split()))

    print(dfs(arr, N))

# 🤔왜 visited를 안에 둔 걸까?
'''
🔥 정리!!!!!
✅ DFS 바깥에 visited를 두는 경우:
✔ 그래프 탐색처럼 여러 개의 연결 요소를 방문할 때!!!!
✔ DFS가 서로 다른 영역을 탐색할 때 공유해야 함!!!!!

✅ 순열 사이클에서는 visited를 DFS 안에서 체크하는 이유:
✔ 각 DFS 탐색이 "하나의 사이클"을 완성하는 역할!!!!
✔ 그래서 DFS는 사이클을 따라가면서 visited만 체크하면 됨!!!!!
✔ 그러나 바깥에 둬도 무방함!! (안에 두면 실행시간 아주 조금 줄어드는 듯!)
'''