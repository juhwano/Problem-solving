def solution(arr1, arr2):
    # 먼저, 두 개의 리스트를 더한 결과를 저장할 2차원 리스트를 만듭니다.
    # 이때, 리스트의 크기는 arr1의 크기와 동일하게 합니다.
    # len(arr1)는 arr1의 행의 개수를, len(arr1[0])는 arr1의 열의 개수를 나타냅니다. 
    # **2차원 리스트는 반드시 리스트 컴프리헨션으로 초기화**
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]

    # arr1의 모든 요소를 순회합니다.
    for i in range(len(arr1)):  # i는 행의 인덱스를 나타냅니다.
        for j in range(len(arr1[i])):  # j는 열의 인덱스를 나타냅니다.
            # arr1의 i행 j열 요소와 arr2의 i행 j열 요소를 더한 값을 answer의 i행 j열에 저장합니다.
            answer[i][j] = arr1[i][j] + arr2[i][j]

    # 두 리스트를 더한 결과를 반환합니다.
    return answer