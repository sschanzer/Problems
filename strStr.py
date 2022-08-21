#! /usr/bin/env python3

'''
Implement strStr().

Given two strings needle and haystack, return the index of the 
first occurrence of needle in haystack, or -1 if needle is not 
part of haystack.

Clarification:

What should we return when needle is an empty string? This is a 
great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is 
an empty string. This is consistent to C's strstr() and Java's 
indexOf().

Input: haystack = "hello", needle = "ll"
Output: 2
'''

def strStr(haystack: str, needle: str) -> int:

    return haystack.find(needle)


if __name__ == '__main__':
    print(strStr('hello', 'll'))
    # 2
    print(strStr('aaaaa', 'bba'))
    # -1
    

        

