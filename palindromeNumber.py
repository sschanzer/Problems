#! /usr/bin/env python3

'''
Palindrome Number
'''

def isPalindrome(x: int) -> bool:
    
    self = str(x)
    lst = [int(i) for i in self]
    
    if lst == lst[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    print(isPalindrome(121))
    print(isPalindrome(123456))
    print(isPalindrome(9876543456789))