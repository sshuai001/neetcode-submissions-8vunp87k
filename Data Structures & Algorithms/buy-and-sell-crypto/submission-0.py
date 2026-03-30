class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        max_profit = 0
        for R in range(1,len(prices)):
            if prices[L] > prices[R]:
                L = R
            #找买入点或者卖出
            else:
                max_profit = max(max_profit,(prices[R] - prices[L]))
        return max_profit