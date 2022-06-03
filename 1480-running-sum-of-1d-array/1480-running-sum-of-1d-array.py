class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = 0
        ans_arr = []
        for i in nums:
            ans += i
            ans_arr.append(ans)
        
        return ans_arr