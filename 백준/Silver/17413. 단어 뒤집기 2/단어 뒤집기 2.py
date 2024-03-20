S = input()
word = ''
tag = False
result = ''

for char in S:  # 문자열 S의 각 문자에 대해 반복
    if char == '<':  # 만약 현재 문자가 '<'라면
        tag = True  # 태그 안에 들어갔다는 것을 표시
        result += word[::-1]  # 지금까지 모인 단어를 뒤집어서 결과 문자열에 추가
        word = ''  # 단어를 초기화
    elif char == '>':  # 만약 현재 문자가 '>'라면
        tag = False  # 태그에서 나왔다는 것을 표시
        result += '>'  # '>'를 결과 문자열에 추가
        continue  # 다음 문자로 넘어감

    if tag:  # 만약 태그 안에 있다면
        result += char  # 현재 문자를 결과 문자열에 그대로 추가
    else:  # 태그 밖에 있다면
        if char == ' ':  # 만약 현재 문자가 공백이라면
            result += word[::-1] + ' '  # 지금까지 모인 단어를 뒤집어서 결과 문자열에 추가하고 공백 추가
            word = ''  # 단어를 초기화
        else:  # 현재 문자가 공백이 아니라면
            word += char  # 현재 문자를 단어에 추가

result += word[::-1]  # 마지막에 모인 단어를 뒤집어서 결과 문자열에 추가
print(result)  # 결과 문자열 출력
