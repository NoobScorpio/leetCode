class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        el = {}
        for i in nums:
            if i not in el:
                el[i] = 1
            else:
                el[i] = el[i] +1
        
        return max(el, key=lambda k: el[k])