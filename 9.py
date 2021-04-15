"""
Palindrome Number

1st Submission:
Runtime: 100 ms, faster than 5.51% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.1 MB, less than 92.48% of Python3 online submissions for Palindrome Number.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x_list = list(str(x))
        temp_list = []
        checker = False
        counter = len(x_list)
            
        for i in range(len(x_list) - 1, -1, -1):
            temp_list.append(x_list[i])
            
        print(temp_list)
        print(x_list)
        
        for i in range(0, len(x_list), 1):
            if x_list[i] == temp_list[i]:
                checker = True
            else:
                checker = False
                return checker
            
        return checker
            
            