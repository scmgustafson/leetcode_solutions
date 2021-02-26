"""
Jewels and Stones
1st Submission:
Runtime: 24 ms, faster than 31.56% of Python online submissions for Jewels and Stones.
Memory Usage: 13.4 MB, less than 61.96% of Python online submissions for Jewels and Stones.
"""
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        counter = 0
        
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if (stones[j] == jewels[i]):
                    counter += 1
        return counter