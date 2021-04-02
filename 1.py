"""
Two Sum

1st Submission:
Runtime: 496 ms, faster than 5.05% of Python3 online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 44.57% of Python3 online submissions for Two Sum.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        output = []
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums), 1):
                if (nums[i] + nums[j]) == target:
                    output.append(i)
                    output.append(j)
        
        return output