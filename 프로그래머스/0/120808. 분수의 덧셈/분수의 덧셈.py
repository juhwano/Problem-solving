def LCM(x,y):
    return (x*y)//GCD(x,y)

def GCD(x,y):
    while y:
        x, y = y, x % y
    return x
    
def solution(numer1, denom1, numer2, denom2):
    arr = [0] * 2
    lcm = LCM(denom1, denom2)
    arr[0] = ((lcm//denom1)*numer1 + (lcm//denom2)*numer2)
    arr[1] = lcm
    gcd = GCD(arr[0], arr[1])
    arr[0] = arr[0]/gcd
    arr[1] = arr[1]/gcd
    answer = arr
    return answer