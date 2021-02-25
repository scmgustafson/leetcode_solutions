"""
How Many Numbers Are Smaller Than the Current Number

1st accepted submission:
Runtime: 620 ms, faster than 5.13% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
Memory Usage: 13.6 MB, less than 38.55% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
"""

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        countlist = []
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if (nums[j] != nums[i]) and (nums[j] < nums[i]):
                    count += 1
            countlist.append(count)
        return countlist