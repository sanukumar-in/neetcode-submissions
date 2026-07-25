class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        finalSum = nums[0]
        currentSum = 0

        for num in nums:
            if currentSum < 0:
                currentSum = 0
             
            currentSum += num
            finalSum = max(finalSum, currentSum)

        return finalSum