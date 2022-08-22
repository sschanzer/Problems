#! /usr/bin/env python3

'''
Given a string s consisting of words and spaces, 
return the length of the last word in the string.

A word is a maximal substring consisting of non-space 
characters only.

Input: s = "Hello World"
Output: 5

Input: s = "   fly me   to   the moon  "
Output: 4

Input: s = "luffy is still joyboy"
Output: 6
'''

def lengthOfLastWord(s: str) -> int:

  slist = s.strip().split(' ')
  last_word = slist[-1]
  llw = len(last_word)

  return llw

if __name__ == '__main__':
    print(lengthOfLastWord("Hello World"))
    # 5
    print(lengthOfLastWord("   fly me   to   the moon  "))
    # 4
    print(lengthOfLastWord("luffy is still joyboy"))
    # 6