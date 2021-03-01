"""
Kids with the Greatest Number of Candies

1st Submission:
Runtime: 32 ms, faster than 22.00% of Python online submissions for Kids With the Greatest Number of Candies.
Memory Usage: 13.5 MB, less than 15.65% of Python online submissions for Kids With the Greatest Number of Candies.
"""
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        outputlist = []
        
        
        for i in range(0, len(candies)):
            for j in range(0, len(candies)):
                newval = (candies[i] + extraCandies)
                
                if newval >= candies[j]:
                    ticker = 1
                else:
                    ticker = 0
                    break
                
            outputlist.append(ticker)
        return outputlist