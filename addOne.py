#! /usr/bin/env python3 

'''
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are 
ordered from most significant to least significant in left-to-right 
order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of 
digits.

Input: digits = [1,2,3]
Output: [1,2,4]

Input: digits = [4,3,2,1]
Output: [4,3,2,2]

Input: digits = [9]
Output: [1,0]
'''

def addOne(digits: list):

  if digits[-1] < 9:
    digits[-1] += 1
    return digits

  if digits[-1] == 9:
    for i in digits:
      strDigits = "".join(str(i) for i in digits)
      nowDigits = int(strDigits) + 1
      for j in strDigits:
        res = [int(j) for j in str(nowDigits)]
 
  return res


if __name__ == '__main__':
    print(addOne([1,2,3]))
    # [1,2,4]
    print(addOne([4,3,2,1]))
    # [4,3,2,2]
    print(addOne([9]))
    # [1,0]
    print(addOne([9,9]))
    # [1,0,0]
    print(addOne([9,9,9]))
    # [1,0,0,0]