# Solution for Leetcode Problem : twoSum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            index2=index+1
            
            while(index2<=len(nums)-1):
                if nums[index]+nums[index2]==target:
                    return [index,index2]
                    
                index2=index2+1
