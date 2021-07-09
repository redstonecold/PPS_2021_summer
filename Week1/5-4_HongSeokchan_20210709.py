'''
https://leetcode.com/problems/day-of-the-year/
'''

class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """ 
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        y,m,d= [int(x) for x in date.split('-')]
        result = sum(days[:m-1]) + d
        if m > 2 and (y%400 == 0 or (y%4 == 0 and y%100 != 0)) :
            result += 1
        return result
            

a = Solution()
date = "2003-03-01"
print(a.dayOfYear(date))