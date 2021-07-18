'''
https://leetcode.com/problems/pascals-triangle/ 
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = list()
        for i in range(1,numRows+1) :
            row = list()
            for j in range(i) :
                if j == 0 or j == i-1 :
                    row.append(1)
                else : row.append(ans[i-2][j-1] + ans[i-2][j])
            ans.append(row)
        return ans

a = Solution()
numRows = 5
print(a.generate(numRows))
    