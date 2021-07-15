"""
Concatenation of Array
1st Submission:
Runtime: 84 ms, faster than 87.83% of Python3 online submissions for Concatenation of Array.
Memory Usage: 14.5 MB, less than 83.32% of Python3 online submissions for Concatenation of Array.
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [num for num in nums]
        
        for i in range(len(ans)):
            ans.append(ans[i])
        
        return ans