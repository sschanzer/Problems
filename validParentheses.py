#! /usr/bin/env python3

'''
Valid Parentheses 
'''

def isValid(s: str) -> bool:

  left_paren = []
  
  for i in s:
    if i in ['(', '[', '{']:
      left_paren.append(i)
    elif i == ')' and len(left_paren) != 0 and left_paren[-1] == '(':
      left_paren.pop()
    elif i == ']' and len(left_paren) != 0 and left_paren[-1] == '[':
      left_paren.pop() 
    elif i == '}' and len(left_paren) != 0 and left_paren[-1] == '{':
      left_paren.pop()
    else:
      return False
  


  return left_paren == []


if __name__ == '__main__':
    print(isValid('()'))
    print(isValid('{[{[()]}]}'))
    print(isValid('{[])'))