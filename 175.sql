"""
Combine Two Tables

1st Submission:
Runtime: 384 ms, faster than 20.90% of MySQL online submissions for Combine Two Tables.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.
"""

SELECT FirstName, LastName, City, State FROM Person
LEFT JOIN  Address
ON Person.PersonID=Address.PersonID;
