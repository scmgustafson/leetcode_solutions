"""
Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

class Solution:
    def reverse(self, x: int) -> int:
        
        limit = 2**31
        
        if x == 0:
            return 0
        else:
            string_x = str(x)
            list = [number for number in string_x]
            list.reverse()

            active = True
            while active:
                if list[0] == "0":
                    list.pop(0)
                else:
                    active = False

            if list[-1] == "-":
                dash = list.pop(-1)
                list.insert(0, dash)

            output = ""

            for number in list:
                output += str(number)
                
            output = int(output)
                
            if output > limit-1 or output < -limit:
                return 0
            else:
                return output