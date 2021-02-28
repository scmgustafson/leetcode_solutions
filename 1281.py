"""
Subtract the Product and Sum of Digits of an Integer

1st Submission:
Runtime: 8 ms, faster than 98.85% of Python online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 13.2 MB, less than 99.49% of Python online submissions for Subtract the Product and Sum of Digits of an Integer.
"""
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        nproduct = 1
        nsum = 0
        ndifference = 0
        nstr = str(n)
        
        for i in range(len(nstr)):
            nproduct *= int(nstr[i])
            nsum += int(nstr[i])

        ndifference = nproduct - nsum
        
        return ndifference
        