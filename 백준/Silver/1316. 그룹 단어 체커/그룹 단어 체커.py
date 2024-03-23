import sys
input = sys.stdin.readline

N = int(input())  # 사용자로부터 숫자를 입력받아 N에 저장
count = 0  # 그룹 단어의 개수를 세는 변수

for _ in range(N):
    word = input().strip()  # N개의 단어를 입력받아 word에 저장
    if list(word) == sorted(word, key=word.find):  # 단어가 그룹 단어인지 확인하는 부분입니다. 단어의 문자들을 그 문자가 처음 나타나는 위치를 기준으로 정렬했을 때 원래의 단어와 같아야 그룹 단어입니다. 이를 확인하기 위해 sorted 함수를 사용하고, key 매개변수로 word.find를 사용하여 각 문자를 그 문자가 처음 나타나는 위치를 기준으로 정렬합니다. 만약 정렬된 단어가 원래의 단어와 같다면, 그 단어는 그룹 단어이므로 count를 1 증가
        count += 1

print(count)  # 그룹 단어의 개수를 출력
