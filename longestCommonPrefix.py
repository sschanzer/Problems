#! /usr/bin/env python3

'''
Longest Common Prefix
'''

def longestCommonPrefix(strs) -> str:

  prefix = ''
  sorted_strs = sorted(strs, key = len)
  min_word = sorted_strs[0]
  
  for i in range(len(min_word)):
    current = strs[0][i]
    # print(current)
    for k in range(len(strs)):
      if strs[k][i] != current:
        return prefix
    prefix += current 

  return prefix


if __name__ == '__main__':
    print(longestCommonPrefix(['flower', 'flow', 'flight']))
    print(longestCommonPrefix(["flower","flower","flower","flower"]))
    print(longestCommonPrefix(['ab', 'a']))
    print(longestCommonPrefix(["dog","racecar","car"]))
    print(longestCommonPrefix(["someone","somewhere","something", "somehow"]))