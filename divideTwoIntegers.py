def divide(dividend: int, divisor: int) -> int:

    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        sign = -1
    else:
        sign = 1
    
    dividend = abs(dividend)
    divisor = abs(divisor)
    result = len(range(0, dividend - divisor + 1, divisor))

    if sign == -1:
        result = -result 

    upper_bound = 2**31 - 1
    lower_bound = -(2**31)
    result = min(upper_bound, max(lower_bound, result))

    return result 

if __name__ == '__main__':
    print(divide(10,3))
    # 3
    print(divide(-7,3))
    # -2
    print(divide(-2,2))
    # -1 