class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = sorted(strs, key = len)
        result = ""
        for j in range(len(strs[0])) :
            for i in range(1,len(strs)) :
                if strs[0][j] != strs[i][j] : 
                    return result
            result += strs[0][j]
        return result

a = Solution()
strs = ["flower","flow","flight"]
print(a.longestCommonPrefix(strs))