class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        countlist = []
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if (nums[j] != nums[i]) and (nums[j] < nums[i]):
                    count += 1
            countlist.append(count)
        return countlist