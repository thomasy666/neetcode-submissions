class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest = 100
        for i, p in enumerate(prices):
            smallest = min(p, smallest)
            profit = max(profit, p - smallest)
        return profit