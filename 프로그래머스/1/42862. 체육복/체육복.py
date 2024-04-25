def solution(n, lost, reserve):
    # 각 학생의 체육복 수를 나타내는 배열 초기화
    uniforms = [1] * (n + 1)  # 학생 번호가 1부터 시작하므로 n + 1 크기로 생성
    
    # 도난 당한 학생 처리
    for l in lost:
        uniforms[l] -= 1
    
    # 여벌 체육복을 가진 학생 처리
    for r in reserve:
        uniforms[r] += 1
    
    # 체육복 빌려주기 처리
    for i in range(1, n + 1):
        if uniforms[i] == 0:  # 체육복이 없는 학생 찾기
            if i > 1 and uniforms[i - 1] > 1:
                uniforms[i - 1] -= 1  # 앞 번호 학생이 여벌 체육복을 줄 수 있다면
                uniforms[i] += 1
            elif i < n and uniforms[i + 1] > 1:
                uniforms[i + 1] -= 1  # 뒤 번호 학생이 여벌 체육복을 줄 수 있다면
                uniforms[i] += 1
    
    # 체육 수업을 들을 수 있는 학생 수 계산
    answer = len([1 for i in range(1, n + 1) if uniforms[i] > 0])
    
    return answer
