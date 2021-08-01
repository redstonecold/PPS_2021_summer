'''
https://leetcode.com/problems/longest-palindrome/ 
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        temp = list(s)
        temp.sort()
        i = 0
        res = 0
        Flag = False
        while i < len(temp):
            c = temp.count(temp[i])
            if c == len(temp):
                return c
            if c % 2 == 0:
                res += c
            else:
                res += c - 1
                Flag = True
            i += c
        if Flag:
            return res+1
        else:
            return res