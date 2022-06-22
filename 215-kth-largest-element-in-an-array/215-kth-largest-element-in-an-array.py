class Solution(object):
    def findKthLargest(self, nums, k):
        nums = sorted(nums, reverse=True)
        return nums[k-1]
        