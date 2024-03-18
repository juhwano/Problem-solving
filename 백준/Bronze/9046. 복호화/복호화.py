from collections import Counter # Counter를 사용하기 위해 collections 모듈에서 Counter를 가져옴

T = int(input())  # 테스트 케이스의 수 T 입력받음

for _ in range(T): # 테스트 케이스의 수 T만큼 반복
    sentence = input()  # 사용자에게 암호문 입력받음
    counter = Counter(sentence.replace(' ', ''))  # 암호문 공백 제거 후 각 문자의 빈도수 계산
    max_count = max(counter.values())  # 가장 빈번한 문자의 빈도수 찾음
    max_chars = [char for char, count in counter.items() if count == max_count] # 가장 자주 나타나는 문자 찾기
    # 가장 빈번한 문자가 여러 개일 경우 '?' 출력, 아니면 해당 문자 출력
    print('?' if len(max_chars) > 1 else max_chars[0])
