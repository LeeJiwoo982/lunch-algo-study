N = int(input())
for i in range(2*N-1):
    if i < N:
        print(' '*(N-(i+1)) + '*'*(i+1))
    else:
        print(' '*((i+1)-N) + '*'*(N-(i+1-N)))

#################################################
#                                               #
#     다른 다양한 방법이 있는지 GPT 에게 물어봄    #
#                                               #
#################################################


# 방법1. 증가하는 부분과 감소하는 부분 나누기

# N = int(input())

# # 첫 번째 부분: 별이 증가하는 부분
# for i in range(1, N + 1):
#     print(" " * (N - i) + "*" * i)

# # 두 번째 부분: 별이 감소하는 부분
# for i in range(N - 1, 0, -1):
#     print(" " * (N - i) + "*" * i)




# 방법2. list에 넣어두고 list를 출력하기

# N = int(input())
# lines = []

# # 첫 번째 부분: 별이 증가하는 부분
# for i in range(1, N + 1):
#     line = " " * (N - i) + "*" * i
#     lines.append(line)

# # 두 번째 부분: 별이 감소하는 부분
# for i in range(N - 1, 0, -1):
#     line = " " * (N - i) + "*" * i
#     lines.append(line)

# # 리스트에 저장된 내용을 출력
# for line in lines:
#     print(line)


# 방법3. 재귀함수꼴로 풀기
# - 첫번째로 별이 증가하는 부분을 출력
# - 그 다음 별이 감소하는 부분 출력
# - 상하가 서로 같은 꼴이므로 상 하를 만들어두고 중간을 재귀꼴로 채우는 형태

# def print_star(n, current):
#     if current > n: # 범위를 벗어나면 탈출, 기본 조건건
#         return
#     print(" " * (n - current) + "*" * current) # 위쪽
#     print_star(n, current + 1) # 가운데는 재귀로
#     print(" " * (n - current) + "*" * current) # 아래쪽

# N = int(input())
# print_star(N, 1)


# 방법4. 프린트 부분을 다른 방식으로 출력

# N = int(input())

# # 첫 번째 부분: 별이 증가하는 부분
# for i in range(1, N + 1):
#     print(f"{' ' * (N - i)}{'*' * i}")

# # 두 번째 부분: 별이 감소하는 부분
# for i in range(N - 1, 0, -1):
#     print(f"{' ' * (N - i)}{'*' * i}")



# 결론:
#     - 증가하는 부분, 감소하는 부분으로 범위를 나눠서 생각하면 식이 조금 더 편하다.
#     - 큰 틀에서 재귀적으로 만드는 방식도 있다.
