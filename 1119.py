"""
Remove Vowels from a String

1st Submission:
Runtime: 32 ms, faster than 53.43% of Python3 online submissions for Remove Vowels from a String.
Memory Usage: 14.2 MB, less than 72.63% of Python3 online submissions for Remove Vowels from a String.
"""

class Solution:
    def removeVowels(self, s: str) -> str:
        
        vowels = ["a", "e", "i", "o", "u"]
        output = ""
        s_list = list(s)

        for i in range(len(s_list)):
            if s_list[i] not in vowels:
                output += s_list[i]
                
        return output