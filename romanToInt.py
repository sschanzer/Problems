#! /usr/bin/env python3

'''
Roman Numeral Converter
'''


def romanToInt(s: str) -> int:
  
  d1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }

  values = []

  for i in range(len(s)):
    #print(i)
    for k, v in d1.items():
      #print(k,v)
      if s[i] == k:
        values.append(v)
  
  # print(values)

  # CD and CM case
  for i in range(1, len(values)):
    if (values[i - 1] == 100 and values[i] == 500) or (values[i - 1] == 100 and values[i] == 1000):           
      values[i - 1] = values[i] - values[i - 1]
      values[i] = 0

  # print(values)


  # XL and XC case
  for i in range(1, len(values)):
    if (values[i - 1] == 10 and values[i] == 50) or (values[i - 1] == 10 and values[i] == 100):           
      values[i - 1] = values[i] - values[i - 1]
      values[i] = 0
  
  
  # IV and IX case
  for i in range(1, len(values)):
    if (values[i - 1] == 1 and values[i] == 5) or (values[i - 1] == 1 and values[i] == 10):           
      values[i - 1] = values[i] - values[i - 1]
      values[i] = 0

  
  return sum(values)


if __name__ == '__main__':
    print(romanToInt('MMCCCXCIX'))
    print(romanToInt('MCMXCIV'))
    print(romanToInt('CDXIV'))
    print(romanToInt('CMDIX'))
    print(romanToInt('LXI'))
    print(romanToInt('XCL'))
    print(romanToInt('IX'))
    print(romanToInt('XIV'))