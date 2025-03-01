#별찍기 21번
#예제로 규칙을 유추해서 별을 찍어라
'''
*       #1

*       #2 row=4,
 *
*
 *

* *     #3
 *
* *
 *
* *
 *

* *     #4
 * *
* *
 * *
* *
 * *
* *
 * *
'''

#규칙 추측
## 예시에서 세로길이는 1> 4> 6> 8
## 공백포함해서 가로갈이는 1> 2> 3> 4
## 인덱스번호 0부터 시작 홀수줄은 공백시작, 짝수줄은 별시작. 그리고 별공백 변갈아
# 입력 1의 경우 실제 세로길이는 2인데 2번째 줄은 공백이 찍히면서 없어진듯.

# 입력값 받RL
N = int(input())
# 행 먼저 순회, 행은 입력값의 두배. 홀수, 짝수일 때 출력이 다르다
# for i in range(2*N):
#     # 열 순회 별과 공백이 번갈아 출력
#         # 행이 0이나 짝수일 때
#     if i%2 == 0:
#         print('* '*(N//2))#1일때 0이 나옴ㅎㅎ
#         # 뒷줄공백은 제거한다고 생각하고
#         # 입력 (1,2)(3,4)가 같은 값을 출력함. 공백이라...N//2 몫이 같은경우
#     # 행이 홀수일 때
#     else:
#         #입력(1)(2,3)(4,5) 가 같은 값 출력.
#         print(' *'*((N+1)//2))
# 너무 복잡하게 생각...
# 출력형식이 잘못됐다고 함.
for i in range(N):
    print('* '*((N+1)//2))  #이것도 되는군...
    print(' *'*(N//2))
    #간단하게 생각하기

#인터넷 코드
for _ in range(N):
    print('* '*(N-N//2))
    print(' *'*(N//2))