'''
https://leetcode.com/problems/repeated-string-match/ 
'''
class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        answer = len(b) // len(a) + 2
        temp = a * answer
        if b not in temp:
            return -1
        while b in a * (answer-1):
            answer = answer - 1
        return answer

o = Solution()
a = "abcd"
b = "cdabcdab"
print()