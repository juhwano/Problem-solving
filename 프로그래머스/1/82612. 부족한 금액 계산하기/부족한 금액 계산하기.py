def solution(price, money, count):
    result = 0
    totalPrice = 0
    for i in range(count):
        totalPrice += price * (i+1)

    if (money <= totalPrice):
        result = totalPrice - money

    return result


