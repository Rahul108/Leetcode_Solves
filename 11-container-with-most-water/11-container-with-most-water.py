class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        left=1
        right=len(height)
        while left<right:
            temp_ans=(right-left)*min(height[left-1],height[right-1])
            ans=max(temp_ans,ans)
            if height[left-1]>=height[right-1]:
                right -= 1
            else:
                left += 1
        return ans