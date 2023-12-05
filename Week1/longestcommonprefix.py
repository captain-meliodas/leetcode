#Link -> https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = list(zip(*strs))
        res = ""
        for i in temp:
            ele = i[0]
            if len(i) == i.count(ele):
                res+=ele
            else:
                break
        
        return res
