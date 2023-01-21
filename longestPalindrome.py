def longestPalindrome(s:str) -> str:

    result = ''
    res_len = 0

    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len:
                result = s[l : r + 1]
                res_len = r - l + 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len:
                result = s[l: r + 1]
                res_len = r - l + 1
            l -= 1
            r += 1


    return result



if __name__ == '__main__':
    print(longestPalindrome('babad'))
    # bab
    print(longestPalindrome('cbbd'))
    # bb


# The below code was not accepted. I believe it solves the problem, but is too inefficient.
    # result = ''

    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s) + 1):
    #             if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(result):
    #                 result = s[i:j]

    #     return result