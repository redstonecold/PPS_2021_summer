'''
https://leetcode.com/problems/keyboard-row/ 
'''
from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans=[]
        set1=set("qwertyuiop")
        set2=set("asdfghjkl")
        set3=set("zxcvbnm")
        for i in words:
            if set(i.lower()) <= set1:
                ans.append(i)
            elif set(i.lower()) <= set2:
                ans.append(i)
            elif set(i.lower()) <= set3:
                ans.append(i)
        return ans
