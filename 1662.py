"""
Check If Two String Arrays are Equivalent

1st Submission:
Runtime: 16 ms, faster than 91.75% of Python online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 13.5 MB, less than 80.73% of Python online submissions for Check If Two String Arrays are Equivalent.
"""

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        catword1 = ""
        catword2 = ""
        
        for i in range(len(word1)):
            catword1 += word1[i]
        
        for i in range(len(word2)):
            catword2 += word2[i]
            
        if (catword1 == catword2):
            return True
        else:
            return False