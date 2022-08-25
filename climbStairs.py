#! /usr/bin/env python3

'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct 
ways can you climb to the top?

Input: n = 2
Output: 2

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

def climbStairs(n : int):

    a = 0       # initialize a to 0
    b = 1       # initialize b to 1

    for i in range(n):      # do the following i times; i.e. 0,1,..., n-1
        c = a + b           # placeholder for next term
        a = b               # a is now b, i.e. if a = 3 and b = 5, a = 5
        b = c               # b is now the next term in the sequence, i.e. if a = 5 and b = 8, b = 13

    return b


if __name__ == '__main__':
    print(climbStairs(2))
    # 2
    print(climbStairs(3))
    # 3
    print(climbStairs(4))
    # 5
    print(climbStairs(5))
    # 8
    print(climbStairs(6))
    # 13
    print(climbStairs(7))
    # 21
  
