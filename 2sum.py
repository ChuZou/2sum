class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1: #verify the given list
            return False
        diff = {} #set up a dictionary
        for i in range(len(nums)): #assume len(list)=3, range(len(list))=[0,1,2] same order as indices of the list
            if nums[i] in diff:
                return [diff[nums[i]], i] #have found the exact difference between target which means we get the required two sum, return
                                          #corresponding indices value.
            else:
                diff[target - nums[i]] = i #if there is no corresponding number in the dic, make the curren difference as key for the dic. 
