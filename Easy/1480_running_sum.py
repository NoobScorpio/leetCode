from typing import List


class Solution:
    def runningSum( nums: List[int]) -> List[int]:
        sums = []
        for i in range(0,len(nums)):
            if i == 0:
                sums.append(nums[i])
            else:
                sums.append(sums[i-1]+nums[i])    
        
        return sums
    
print(Solution.runningSum(nums=[1,2,3,4]))
print(Solution.runningSum(nums=[1,1,1,1,1]))
print(Solution.runningSum(nums=[3,1,2,10,1]))