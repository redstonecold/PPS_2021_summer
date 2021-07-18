'''
https://leetcode.com/problems/plus-one/ 
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = list(str(int("".join(list(map(str, digits)))) + 1))
        return list(map(int,digits))
        

a = Solution()
digits = [4,3,2,1]
print(a.plusOne(digits))
