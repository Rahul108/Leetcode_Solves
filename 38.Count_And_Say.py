class Solution:
    def countAndSay(self, n: int) -> str:
        res_str = '1'
        for i in range(n-1):
            check_char = res_str[0]
            temp_result = ''
            count = 0
            for j in res_str:
                if j == check_char:
                    count += 1
                else:
                    temp_result += str(count) + check_char
                    count = 1
                    check_char = j
            temp_result += str(count) + check_char
            res_str = temp_result
        return res_str