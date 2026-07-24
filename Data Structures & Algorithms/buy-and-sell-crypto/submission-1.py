class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxPro = 0

        for sell in prices:
            profit = sell - minBuy
            maxPro = max(maxPro, profit)
            minBuy = min(minBuy, sell)


        return maxPro