'''
https://leetcode.com/problems/backspace-string-compare/ 
'''
from collections import deque
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = deque()
        dt = deque()
        for ch in s :
            if ch == '#' :
                if len(ds) > 0 :
                    ds.pop()
            else : ds.append(ch)
        for ch in t :
            if ch == '#' :
                if len(dt) > 0 :
                    dt.pop()
            else : dt.append(ch)
        if list(ds) == list(dt) :
            return True
        return False

a = Solution()
s = "ab##"
t = "c#d#"
print(a.backspaceCompare(s,t))