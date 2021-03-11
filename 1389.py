"""
Create Target Array in the Given Order

1st Submission:
Runtime: 28 ms, faster than 13.73% of Python online submissions for Create Target Array in the Given Order.
Memory Usage: 13.4 MB, less than 41.28% of Python online submissions for Create Target Array in the Given Order.
"""

class Solution(object):
    def createTargetArray(self, nums, index):
        output = []
        
        for i in range(len(nums)):
            output.insert(index[i], nums[i])
        
        return output