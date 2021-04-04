"""
Add Strings

1st Submission:
Runtime: 36 ms, faster than 78.75% of Python3 online submissions for Add Strings.
Memory Usage: 14.5 MB, less than 41.00% of Python3 online submissions for Add Strings.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        summation = int(num1) + int(num2)
        
        return str(summation)