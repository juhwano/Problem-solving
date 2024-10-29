from collections import Counter
def solution(a, b, c, d):
    count_arr=Counter([a,b,c,d])
    score=0
    max_counter = count_arr.most_common(1)[0][1]
    reverse_dict = {value:key for key,value in count_arr.items()}
    
    if max_counter == 4:
        score += 1111*a
    elif max_counter == 3:
        one_num = reverse_dict.get(1)
        three_num = reverse_dict.get(3)
        score += (10 * three_num + one_num)**2
    elif max_counter == 2:
        value_one = count_arr.most_common(2)[0][1]
        value_two =count_arr.most_common(2)[1][1]
        
        if value_one == value_two:
            key_one =count_arr.most_common(2)[0][0]
            key_two =count_arr.most_common(2)[1][0]
            score += (key_one + key_two) * abs(key_one - key_two)
        else:
            key_one =count_arr.most_common(3)[0][0]
            key_two =count_arr.most_common(3)[1][0]
            key_three =count_arr.most_common(3)[2][0]
        
            score += (key_two * key_three)
    else:
        arr =count_arr.most_common()
        sort_arr = sorted(arr)
        min_num = sort_arr[0][0]
        
        score += min_num

    return score