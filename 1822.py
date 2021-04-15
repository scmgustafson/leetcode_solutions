"""
Sign of the Product of an Array

1st Submission:
Runtime: 60 ms, faster than 79.99% of Python3 online submissions for Sign of the Product of an Array.
Memory Usage: 14.4 MB, less than 39.04% of Python3 online submissions for Sign of the Product of an Array.
"""

class Solution:
    def arraySign(self, nums: List[int]) -> int:

        if nums[0] > 0:
            running_prod = 1
        elif nums[0] < 0:
            running_prod = -1
        elif nums[0] == 0:
            return 0
        
        for i in range(1, len(nums), 1):
            if nums[i] == 0:
                return 0
            elif nums[i] > 0:
                running_prod *= 1
            elif nums[i] < 0:
                running_prod *= -1
                
        return running_prod