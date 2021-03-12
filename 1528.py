"""
Shuffle String

1st Submission:
Runtime: 44 ms, faster than 48.43% of Python online submissions for Shuffle String.
Memory Usage: 13.4 MB, less than 91.42% of Python online submissions for Shuffle String.
"""

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        list = [""] * len(s)
        output = ""
        
        for i in range(len(s)):
            list[indices[i]] = s[i]
        
        for i in range(len(list)):
            output += list[i]
        
        return output