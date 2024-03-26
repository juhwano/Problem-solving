# 후위 표기식(Postfix notation)은 연산자를 피연산자 뒤에 표기하는 방식
# 장점 : 괄호를 사용하지 않아도 연산의 우선순위를 명확하게 표시 가능

# 스택을 이용하여 후위 표기식을 계산 가능

import sys
input = sys.stdin.readline

n = int(input())  # 피연산자의 개수를 입력받습니다.
expression = input().strip()  # 후위 표기식을 입력받습니다.
values = [0]*n  # 피연산자에 대응하는 값들을 저장할 리스트를 생성합니다.
for i in range(n):  # 각 피연산자에 대응하는 값을 입력받습니다.
    values[i] = int(input())
stack = []  # 계산을 위한 스택을 생성합니다.
for i in expression:  # 후위 표기식의 각 문자에 대해 반복합니다.
    if i.isalpha():  # 문자가 알파벳인 경우
        stack.append(values[ord(i) - ord('A')])  # 해당 알파벳에 대응하는 값을 스택에 추가합니다.
    else:  # 문자가 연산자인 경우
        a = stack.pop()  # 스택에서 두 개의 피연산자를 꺼냅니다.
        b = stack.pop()
        if i == '+':  # 연산자에 따라 적절한 연산을 수행하고 결과를 스택에 추가합니다.
            stack.append(b + a)
        elif i == '-':
            stack.append(b - a)
        elif i == '*':
            stack.append(b * a)
        elif i == '/':
            stack.append(b / a)

print(f"{stack[0]:.2f}")  # 최종 결과를 소수점 둘째 자리까지 출력합니다.
