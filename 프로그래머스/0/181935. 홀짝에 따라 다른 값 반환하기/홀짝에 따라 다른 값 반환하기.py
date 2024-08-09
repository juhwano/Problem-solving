def solution(n):
    sum = 0
    if n % 2 != 0:
        for i in range(n+1):
            if i % 2 != 0:
                sum+=i
    else:
        for i in range(n+1):
            if i % 2 == 0:
                sum+=i**2
        
    return sum