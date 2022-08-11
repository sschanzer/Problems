#! /usr/bin/env python3

'''
A phrase is a palindrome if, after converting all uppercase 
letters into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward and backward. Alphanumeric 
characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

def isPalindrome(s : str):

    slist = []

    for i in s:
        if i.isalnum():
            slist.append(i.lower())

    if slist == slist[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama"))
    # True
    print(isPalindrome("race a car"))
    # False
    print(isPalindrome(" "))
    # True

    