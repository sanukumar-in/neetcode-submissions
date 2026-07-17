class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}

        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        
        numList = []
        for num in numCount:
            numList.append([num, numCount[num]])
            numList.sort(key=lambda x: x[1], reverse=True)

        ans = []
        for i in range(k):
            ans.append(numList[i][0])

        return ans