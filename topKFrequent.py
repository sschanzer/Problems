'''
Given an integer array nums and an integer k, 
return the k most frequent elements.
You may return the answer in any order.
'''


def topKFrequent(nums, k):

  count_dict = {}
  res = []

  for i in nums:
    if i in count_dict:
      count_dict[i] += 1
    else:
      count_dict[i] = 1

  for j in range(k):
    greatest = max(count_dict, key = lambda x : count_dict[x])
    res.append(greatest)
    count_dict[greatest] = 0 

  return res


if __name__ == '__main__':
    print(topKFrequent([1,1,1,2,2,3], 2))
    # [1,2]
    print(topKFrequent([1], 1))
    # [1]
    print(topKFrequent([-1,-1], 1))
    # [-1]
    print(topKFrequent([3,0,1,0], 1))
    # [0]




# ALTERNATIVE SOLUTION

# def topKFrequent(nums, k):

#     count_dict = {}
#     # make array of buckets, where each bucket represents a frequency and contains all elements that have that frequency.
#     # i.e. the first bucket buckets[1] contains all elements that have a frequency of 1
#     buckets = [[] for n in range(len(nums) + 1)]
#     res = []

#     # construct counter dict
#     for i in nums:
#         count_dict[i] = nums.count(i)
    
#     for key, val in count_dict.items():
#         buckets[val].append(key)

#     # traverse the list from last to first
#     for j in range(len(nums), 0, -1):
#         if buckets[j]:
#             res.extend(buckets[j])
#         if len(res) == k:
#             break
    
#     return res[:k]
