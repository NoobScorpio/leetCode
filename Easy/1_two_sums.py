class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        i = 0
        while i < len(nums):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff],i]
            else:
                seen[nums[i]] = i
            i += 1

