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
            
"""
Palindrome Number

2nd submission:
Runtime: 80 ms, faster than 24.04% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.1 MB, less than 76.68% of Python3 online submissions for Palindrome Number.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_list = [i for i in x_str]

        reversed_x_list = []
        for i in range(len(x_list)-1, -1, -1):
            reversed_x_list.append(x_list[i])
        
        reversed_x_str = ""
        for i in reversed_x_list:
            reversed_x_str += i
            
        output = None
        
        if x_str == reversed_x_str:
            output = True
        else:
            output = False
        
        return output