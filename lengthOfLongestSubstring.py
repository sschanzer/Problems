def lengthOfLongestSubstring(s:str) -> int:
    
    letter_set = set()
    i = 0
    j = 0
    maxLen = 0

    while j < len(s):                       # this will go through all characters of s
        if s[j] not in letter_set:          # if the letter is not in the letter set
            letter_set.add(s[j])            # add the letter to the set
            j += 1                          # move j to the right by one letter
        else:
            letter_set.remove(s[i])         # if s[j] is in letter set, remove its earlier occurance by removing s[i] 
            i += 1                          # now move s[i] to the right
            
        maxLen = max(maxLen, j - i)         # take the max of maxLen and j - i for the max length of the substring
    
    return maxLen

if __name__ == "__main__":
    print(lengthOfLongestSubstring('abcabcbb'))
    # 3
    print(lengthOfLongestSubstring('bbbbbbb'))
    # 1
    print(lengthOfLongestSubstring('pwwkew'))
    # 3


