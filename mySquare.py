#! /usr/bin/env python3

'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, 
and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or 
operator, such as pow(x, 0.5) or x ** 0.5.

Input: x = 4
Output: 2

Input: x = 8
Output: 2
'''

def mySquare1(x: int) -> int:

    r = x 

    while r * r > x:
        r = (r + x // r) // 2 # Newton's Method with integer division

    return r        # Returns integer


def mySquare2(x: int) -> float:

    r = x 

    while r * r > x:
        r = (r + x / r) / 2   # Newton's Method 

    return r            # Returns approximation of square root


if __name__ == '__main__':
    print(mySquare1(4))
    # 2
    print(mySquare1(8))
    # 2
    print(mySquare2(8))
    # 2.82842712474619
    print(mySquare2(2))
    # 1.414213562373095 