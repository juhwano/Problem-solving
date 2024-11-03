def solution(q, r, code):
    result = []
    for i, v in enumerate(code):
        if i % q == r:        
            result.append(v)
    answer = ''.join(result)
    return answer