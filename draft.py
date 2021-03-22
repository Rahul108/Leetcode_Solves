import sys

def myAtoi(s):
    max_int = 2 ** 31 - 1
    min_int = -2 ** 31
    i=res=0
    sign=1
    l = len(s)
    if l == 0:
        return 0
    
    while i<l and s[i]==' ':
        i+=1
    
    if i<l and (s[i]=='+' or s[i]=='-'):
        sign = 1 if s[i]=='+' else -1
        i+=1
    
    while i<l and s[i]>='0' and s[i]<='9':
        if res > max_int/10 or (res == max_int/10 and (ord(s[i])-ord('0')) > max_int % 10):
            return max_int if sign==1 else min_int
        res = res * 10 + (ord(s[i])-ord('0'))
        i+=1
    
    return res*sign
