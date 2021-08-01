'''
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/
차집합 이용
'''
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        comp = set(range(1,len(nums)+1))
        nums = set(nums)
        return list(comp - nums)

a = Solution()
nums = [4,3,2,7,8,2,3,1]
print(a.findDisappearedNumbers(nums))