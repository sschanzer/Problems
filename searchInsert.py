#! /usr/bin/env python3

'''
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

def searchInsert(nums: list, target: int) -> int:

    # if target is in the list
    for num in nums:
        if num == target:
            return nums.index(target)

    # if target is not in the list
    if target not in nums:
        nums.append(target)
        nums = sorted(nums)
    
    return nums.index(target)

if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 5))
    # 2
    print(searchInsert([1,3,5,6], 2))
    # 1
    print(searchInsert([1,3,5,6], 7))
    # 4
