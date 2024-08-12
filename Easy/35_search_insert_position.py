class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0

        if target <= nums[0]:
            return 0
        while i < len(nums):
            if target > nums[i]:
                if (i+1) == len(nums):
                    return i + 1
                i+=1
            else:
                return i