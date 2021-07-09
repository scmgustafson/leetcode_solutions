"""
FizzBuzz

1st Submission:
Runtime: 32 ms, faster than 98.52% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15.1 MB, less than 21.90% of Python3 online submissions for Fizz Buzz.
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        counter = 0
        output = []
        
        while counter <= n:   
            if counter == 0:
                counter += 1
            elif counter % 3 == 0 and counter % 5 == 0:
                output.append("FizzBuzz")
                counter += 1
            elif counter % 3 == 0:
                output.append("Fizz")
                counter += 1
            elif counter % 5 == 0:
                output.append("Buzz")
                counter += 1
            else:
                output.append(str(counter))
                counter += 1
        
        return output

"""
2nd Submission:
Runtime: 36 ms, faster than 95.55% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15.2 MB, less than 22.12% of Python3 online submissions for Fizz Buzz.
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(f"{i}")
        
        return output