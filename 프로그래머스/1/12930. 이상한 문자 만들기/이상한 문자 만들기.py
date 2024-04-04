def solution(s):
    result = []
    index =0
    
    for char in s:
        if char == ' ':
            result.append(' ')
            index = 0
        else:
            if index % 2 == 0:
                result.append(char.upper())
            else:
                result.append(char.lower())
            index += 1
    
    return ''.join(result)