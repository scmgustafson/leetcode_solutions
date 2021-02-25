"""
Defanging an IP Address

1st submission:
Runtime: 20 ms, faster than 42.64% of Python online submissions for Defanging an IP Address.
Memory Usage: 13.4 MB, less than 90.53% of Python online submissions for Defanging an IP Address.
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        defanged_address_arr = []
        defanged_address_str = ""
        
        for i in range(len(address)):
            if address[i] == ".":
                defanged_address_arr.append("[")
                defanged_address_arr.append(".")
                defanged_address_arr.append("]")
            else:
                defanged_address_arr.append(address[i])
                
        for i in range(len(defanged_address_arr)):
            defanged_address_str += defanged_address_arr[i]
            
        return defanged_address_str