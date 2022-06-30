#! /usr/bin/env python3

'''
LC Two Sum
'''

def twoSum(nums: list[int], target: int) -> list[int]:

    prevMap = {} # val : index

    for i, n in enumerate(nums):
        diff = target - n 
        if diff in prevMap:
            return[prevMap[diff], i]
        prevMap[n] = i
    return




# SLOWER SOLUTION:
        # isSolution = False
        # i = 0

        # solution = []

        # while i < len(nums) and not isSolution:
        #     j = i + 1
        #     while j < len(nums) and not isSolution:
        #         if nums[i] + nums[j] == target:
        #             isSolution = True
        #             solution.append(i)
        #             solution.append(j)
        #         j += 1
        #     i += 1 
        
        # return solution





if __name__ == '__main__':
    print(twoSum(nums = [2,7,11,15], target = 9))