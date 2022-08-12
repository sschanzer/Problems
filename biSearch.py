#! /usr/bin/env python3

'''
Given an array of integers nums which is sorted in ascending 
order, and an integer target, write a function to search target 
\in nums. If target exists, then return its index. Otherwise, 
return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

def biSearch(nums: list, target: int):

    for i in nums:
        if i == target:
            return nums.index(i)
    
    return -1


if __name__ == '__main__':

    print(biSearch([-1,0,3,5,9,12], 9))
    # 4
    print(biSearch([-1,0,3,5,9,12], 2))
    # -1