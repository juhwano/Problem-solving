def solution(arr, queries):
    
    for i in range(len(queries)):
        k,v = queries[i]
        arr[k], arr[v] = arr[v], arr[k]
    
    answer = arr
    return answer