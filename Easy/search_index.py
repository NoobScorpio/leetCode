def searchInsert(nums, target):
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
        

# FIND NUM INDEX
print(searchInsert([1,3,5,6],7))