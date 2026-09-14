class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i,j):

            if j == len(p):
                return i == len(s)

            if(i,j) in memo:
                return memo[(i,j)]

            first_match = (
                i < len(s) and 
                (s[i]==p[j]or p[j]=='.')
            )
            
            if j+1 < len(p) and p[j+1] == '*':

                skip = dp(i,j+2)

                use = first_match and dp(i+1,j)

                result = skip or use

            else:

                result = first_match and dp(i+1,j+1)

            memo[(i,j)]=result
            return result

        return dp(0,0)