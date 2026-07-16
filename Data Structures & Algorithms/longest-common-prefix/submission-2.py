class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            for st in strs:
                if len(st) == i or st[i] != strs[0][i]:
                    return st[:i]
        
        return strs[0]