"""
Count Items Matching a Rule

1st Submission:
Runtime: 248 ms, faster than 51.10% of Python3 online submissions for Count Items Matching a Rule.
Memory Usage: 20.6 MB, less than 65.74% of Python3 online submissions for Count Items Matching a Rule.
"""
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        elif ruleKey == "name":
            index = 2
        
        count = 0
        for item in items:
            if item[index] == ruleValue:
                count += 1
        return count