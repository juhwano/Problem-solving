def solution(array, commands):
    answer = []
    for command in commands:
        if command[0] == command[1]:
            answer.append(array[command[0]-1])
            continue
        start = command[0]-1
        end = command[1]
        newArr= array[start:end]
        newArr.sort()

        if len(newArr) >= command[2]:
            answer.append(newArr[command[2]-1])
        else:
            raise
    return answer