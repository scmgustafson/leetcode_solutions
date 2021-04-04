'''
Best Time to Buy and Sell Stock

1st Submission:
Broke leetcode, will run but can't submit.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            
        maxprofit = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices), 1):
                profit = prices[j] - prices[i]
                
                if profit > maxprofit:
                    maxprofit = profit
        
        return maxprofit