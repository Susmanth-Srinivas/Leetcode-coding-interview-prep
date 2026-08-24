class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n-1):
            result=self.read(result)

        return result
    
    def read(self,s : str)->str:
        next_str = ""
        i=0

        while i <len(s):
            digit=s[i]
            count=0

            while i<len(s) and s[i]== digit:
                count += 1
                i += 1

            next_str += str(count)+ digit

        return next_str