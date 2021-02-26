"""
Shuffle the Array
1st submission (needed help):
Runtime: 40 ms, faster than 93.32% of Python online submissions for Shuffle the Array.
Memory Usage: 13.6 MB, less than 73.47% of Python online submissions for Shuffle the Array.
"""
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        shuffled = []
        
        for i in range(len(nums) / 2):
            shuffled.append(nums[i])
            shuffled.append(nums[i+n])
            
        return shuffled