import sys
input = sys.stdin.readline

N = input().strip()  # 사용자로부터 문자열을 입력받아 N에 저장
word = ''

if '_' in N:  # C++ 형식인 경우
    if N[0] == '_' or N[-1] == '_' or '__' in N or not N.islower():  # 변수명이 '_'로 시작하거나 끝나거나, '__'를 포함하거나 대문자를 포함하면 에러
        word = 'Error!'
    else:
        words = N.split('_')
        for i in range(len(words)):
            if i == 0:
                word += words[i]
            else:
                word += words[i].capitalize()  # 첫 문자를 대문자로 변환
elif N[0].islower():  # Java 형식인 경우
    for i in N:
        if i.isupper():  # 대문자를 '_'와 소문자로 변환
            word += '_' + i.lower()
        else:
            word += i
else:  # 둘 다 아닌 경우
    word = 'Error!'

print(word)