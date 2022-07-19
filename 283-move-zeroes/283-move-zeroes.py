class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=0
        nums_len=len(nums)
        no_of_zero=0
        for i in nums:
            if i!=0:
                nums[j]=i
                j+=1
            else:
                no_of_zero+=1
        for i in range((nums_len-no_of_zero), nums_len):
            nums[i]=0
        return nums
                