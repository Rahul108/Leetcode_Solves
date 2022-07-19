class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_map={}
        left=0
        right=0
        max_length=0
        while right<len(s) and left<len(s):
            if s[right] in string_map:
                left=max(left,string_map[s[right]]+1)
            string_map[s[right]]=right
            max_length=max(max_length, right-left+1)
            right+=1
        return max_length