class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPointer = 0
        rightPointer = 1
        max_profit = 0
        while rightPointer < len(prices):
            buyValue = prices[leftPointer]
            sellValue = prices[rightPointer]
            if buyValue > sellValue:
                leftPointer = rightPointer
                rightPointer += 1
            else:
                profit = sellValue - buyValue
                max_profit = profit if profit > max_profit else max_profit
                rightPointer += 1
        return max_profit