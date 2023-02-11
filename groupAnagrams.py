'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original letters exactly once.
'''

def groupAnagrams(strs):

    result = {}

    # sort the words in the list
    for word in strs:
        word_sorted = ''.join(sorted(word))

        # build result dictionary
        if word_sorted not in result:
            result[word_sorted] = [word]
        else:
            result[word_sorted] += [word]

    return list(result.values())

if __name__ == '__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(groupAnagrams([""]))
    # [[""]]
    print(groupAnagrams(['a']))
    # [['a']]