class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        min_range=self.findMinRange(nums, target)
        max_range=self.findMaxRange(nums, target)
        return [min_range, max_range]
    
    def findMinRange(self, nums: List[int], target:int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                if mid==0 or nums[mid-1]!=target:
                    return mid
                right-=1
            elif nums[mid]<target:
                left+=1
            else:
                right-=1
        return -1
    
    def findMaxRange(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                if mid==len(nums)-1 or nums[mid+1]!=target:
                    return mid
                left += 1
            elif nums[mid]<target:
                left+=1
            else:
                right-=1
        return -1