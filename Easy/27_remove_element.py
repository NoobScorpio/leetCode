class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # Place the non-val element at the current length index
                nums[length] = nums[i]
                length += 1
        return length