class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        buy = prices[0]
        maxp = -1
        for i in range(1, len(prices)):
            profit = prices[i] - buy
            maxp = max(maxp, profit)
            buy = min(buy, prices[i])
        return max(0, maxp) 
