# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:     
        
        # TIMEOUT BRUTE FORCE APPROACH
#         amt_prices = len(prices)
        
#         for i in range(amt_prices):
#             # Calculate profit for each potential sell day
#             for j in range(i+1, amt_prices):
#                 # Skip if sell price lower than buy price
#                 if prices[j] <= prices[i]:
#                     continue
                
#                 # Update variable keeping track of possible max profit
#                 max_profit = max(prices[j] - prices[i], max_profit)
        
#         return max_profit
            
        # 1-pass look for absolute min approach
        min_price = float("inf")    # make the assumption we buy at the lowest price
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            
            profit_if_sold_today = price - min_price
            
            # update maximum possible profit
            max_profit = max(max_profit, profit_if_sold_today)
        
        return max_profit
            