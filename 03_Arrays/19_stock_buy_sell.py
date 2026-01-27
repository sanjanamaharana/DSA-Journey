prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]

buy = float('inf')
sell = 0

class Solution:
    # Function to calculate max profit using brute force
    def stockbuySell(self, prices):
        # Initialize max profit to 0
        maxProfit = 0

        # Loop through each day as potential buy day
        for i in range(len(prices)):
            # Loop through future days as potential sell day
            for j in range(i + 1, len(prices)):
                # Calculate profit
                profit = prices[j] - prices[i]

                # Update max profit if higher
                maxProfit = max(maxProfit, profit)

        # Return the maximum profit
        return maxProfit

# Driver code
sol = Solution()
prices = [7,6,4,3,1]
print("Max Profit:", sol.stockbuySell(prices))










best_p = 0
for i in range(len(prices)):
  
  for j in range(i+1,len(prices)):
    profit = prices[j] - prices[i]
    best_p = max(profit,best_p)
print(best_p)











buy = float('inf')
max_profit = 0

for p in prices:
    buy = min(buy, p)
    max_profit = max(max_profit, p - buy)

print( max_profit)
