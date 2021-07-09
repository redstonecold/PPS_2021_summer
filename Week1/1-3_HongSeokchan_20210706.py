'''
https://leetcode.com/problems/assign-cookies/submissions/ 
testcase 문제가 있는듯?
maximize한 output값을 출력하라 했는데 걸리는 부분이 있음
'''
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        snum = sum(s)
        g = sorted(g)
        count = 0
        for i in range(len(g)) :
            if g[i] > snum : break
            snum -= g[i]
            count += 1
        return count

a = Solution()
g = [1,2,3]; s = [3]
print(a.findContentChildren(g,s))