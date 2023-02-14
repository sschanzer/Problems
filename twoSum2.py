'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be 
numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same 
element twice.

Your solution must use only constant extra space.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

'''

def twoSum(numbers: list, target: int):
    
    l, r = 0, len(numbers) - 1

    while l < r:
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l + 1, r + 1]
        elif sum < target:
            l += 1
        else:
            r -= 1
    return []

if __name__ == '__main__':
    print(twoSum([2,7,11,15], 9))
    # [1,2]
    print(twoSum([2,3,4], 6))
    # [1,3]
    print(twoSum([-1000,-1,0,1], 1))
    # [3,4]
    print(twoSum([-3,3,4,90], 0))
    # [1,2]
    print(twoSum([0,0,3,4], 0))
    # [1,2]








# O(n^2) Not going to work...
# def twoSum(numbers: list, target: int):

#   res = []
  
#   if target == 0:
#     if numbers[0] == 0:
#         res.extend([numbers.index(0) + 1, numbers.index(0) + 2])
#         return res

#   for i in range(len(numbers)):
#       for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#           res.extend([i + 1, j + 1])
  
#   return res