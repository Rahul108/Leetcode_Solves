# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=1
        right=n
        while left<=right and left<=n and right<=n:
            if left==right:
                return left
            mid=(left+right)//2
            if isBadVersion(mid)==True:
                right=mid
            else:
                left=mid+1
        return -1