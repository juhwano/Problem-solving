def solution(arr, queries):
    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
        
        if k == 0:  # k가 0인 경우를 처리
            continue
        
        for i in range(s, e+1):
            if i % k == 0:
                arr[i] += 1
    
    return arr