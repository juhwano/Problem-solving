def solution(number):
    # 시간복잡도 number의 길이, 10^5
    # 풀이방법 O(n) 이하
    lst = list(map(int,number)) # O(n)
    return sum(lst) % 9