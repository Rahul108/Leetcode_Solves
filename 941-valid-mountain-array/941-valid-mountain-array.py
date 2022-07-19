class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        eval_len = 1
        if arr_len < 3:
            return False
        while arr_len > eval_len and arr[eval_len-1]<arr[eval_len]:
            eval_len += 1
        if eval_len == arr_len or eval_len==1:
            return False
        while arr_len > eval_len and arr[eval_len-1]>arr[eval_len]:
            eval_len+=1
        if eval_len != arr_len:
            return False
        return True