class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for st in strs:
            sortSt = "".join(sorted(st))
            res[sortSt].append(st)
        
        return list(res.values())