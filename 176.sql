"""
Second Highest Salary

1st Submission:
Runtime: 168 ms, faster than 86.57% of MySQL online submissions for Second Highest Salary.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.
"""

SELECT MAX(salary) AS "SecondHighestSalary" FROM Employee WHERE salary < (SELECT MAX(salary) FROM Employee);