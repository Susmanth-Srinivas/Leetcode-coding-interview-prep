class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        #lets skip the leading white spaces 
        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        num =0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        

        num *= sign
        INT_MIN, INT_MAX = -2**31,2**31-1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
        