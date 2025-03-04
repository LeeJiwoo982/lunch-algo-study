def star(N):
    if N == 1:
        return ["*"]  # 기본 삼각형 패턴 (N=1일 때)
    
    prev = star(N - 1)  # 이전 단계의 패턴을 재귀적으로 생성
    height = 2 ** N - 1  # 현재 단계 삼각형의 높이 계산
    width = 2 ** (N + 1) - 3  # 현재 단계 삼각형의 너비 계산

    new_pattern = [" " * width for _ in range(height)]  # 공백으로 초기화된 패턴 리스트 생성

    if N % 2 == 1:  # N이 홀수일 때 (위로 뾰족한 삼각형)
        mid = width // 2  # 삼각형의 중앙 위치
        new_pattern[0] = " " * mid + "*" + " " * mid  # 꼭대기 별 하나 배치
        
        # 꼭대기에서 중간까지 삼각형을 확장
        for i in range(1, height//2):
            left_space = " " * (mid - i)  # 왼쪽 공백 계산
            inner_space = " " * (2 * i - 1)  # 내부 공백 계산
            new_pattern[i] = left_space + "*" + (inner_space + "*" if inner_space else "") + left_space
        
        # 이전 단계의 패턴 삽입 (중간 부분)
        for j in range(height//2):
            left_space = " " * (len(prev) - j)  # 왼쪽 공백 계산
            between_space = " " * j  # 별 사이의 공백 계산
            if j < len(prev):
                new_pattern[height//2 + j] = left_space + "*" + between_space + (prev[j]) + between_space + '*' + left_space
        
        # 삼각형의 마지막 줄 (전체 별로 채워짐)
        new_pattern[height-1] = '*' * width
    
    else:  # N이 짝수일 때 (아래로 뾰족한 삼각형)
        new_pattern[0] = "*" * width  # 맨 윗줄 (가장 긴 줄)
        
        # 큰 삼각형의 윗부분 생성
        for i in range(1, height // 2 + 1):
            left_space = " " * i  # 왼쪽 공백 계산
            between_space = " " * (height//2 - i)  # 별 사이의 공백 계산
            if i <= len(prev):
                new_pattern[i] = left_space + "*" + between_space + (prev[i-1]) + between_space + '*' + left_space
        
        # 이전 단계의 패턴 삽입 (중간 부분)
        for j in range(height//2 -1):
            left_space = " " * (height//2 + 1 + j)  # 왼쪽 공백 계산
            between_space = " " * (2 ** N - 5 - 2*j)  # 별 사이의 공백 계산
            new_pattern[height//2 + 1 + j] = left_space + "*" + between_space + '*' + left_space

        # 마지막 줄 (중앙 별 하나만 위치)
        new_pattern[height-1] = ' ' * (width//2) + '*' + ' ' * (width//2)
    
    return new_pattern


N = int(input())  # 사용자 입력 받기

lines = star(N)  # 별 패턴 생성
lines = [l.rstrip() for l in lines]  # 오른쪽 공백 제거

print('\n'.join(lines))  # 최종 결과 출력

# 결과를 파일에 저장 (주석 처리됨)
# with open('result.txt', 'w') as f:
#     f.write("\n".join(lines))
