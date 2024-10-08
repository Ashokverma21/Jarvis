class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i,v in enumerate(nums):
            if(target-v in dc):
                return dic[target-v],i
            dic[v]=i