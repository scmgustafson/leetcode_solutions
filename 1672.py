"""
Richest Customer Wealth

1st: Submission
Runtime: 48 ms, faster than 93.16% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 14.3 MB, less than 27.92% of Python3 online submissions for Richest Customer Wealth.
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        index = None
        top_total = 0
        new_total = 0
        
        for account in accounts:
            new_total = 0
            for money in account:
                new_total += money
                
            if top_total < new_total:
                top_total = new_total
            
        return top_total