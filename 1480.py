"""
Running Sum of 1d Array

1st submission:
Runtime: 24 ms, faster than 80.92% of Python online submissions for Running Sum of 1d Array.
Memory Usage: 13.7 MB, less than 14.64% of Python online submissions for Running Sum of 1d Array.
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sumlist = []
        counter = 0
        
        for i in range(len(nums)):
            counter += nums[i]
            sumlist.append(counter)
        return sumlist