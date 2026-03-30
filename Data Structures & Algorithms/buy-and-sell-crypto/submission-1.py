class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L= 0
        profit = 0
        for R in range(0, len(prices)):
            if prices[L] > prices[R]:
                L = R
            else:
                profit = max(profit, prices[R] - prices[L])
        return profit
