#Link -> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for p in prices:
            current_profit = p - buy_price
            profit = max(profit,current_profit)
            buy_price = min(p,buy_price)
        
        return profit
