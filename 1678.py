"""
Goal Parser Interpretation

1st Submission:
Runtime: 32 ms, faster than 59.65% of Python3 online submissions for Goal Parser Interpretation.
Memory Usage: 14.3 MB, less than 38.28% of Python3 online submissions for Goal Parser Interpretation.
"""

class Solution:
    def interpret(self, command: str) -> str:
        command_list = list(command)
        temp_list = []
        output = ""
        
        for i in range(len(command_list)):
            if command_list[i] == "G":
                temp_list.append("G")
            elif command_list[i] == "(":
                if command_list[i+1] == ")":
                    temp_list.append("o")
                elif command_list[i+1] == "a":
                    temp_list.append("al")
        
        for i in temp_list:
            output += i
            
        return output