def longestPalindrome(s):
        
        longest = ""
        for i in range (len(s)):
            for j in range(i,len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1] and len(substring)>len(longest):
                    longest = substring
        return longest


s = "babad"
print(longestPalindrome(s))