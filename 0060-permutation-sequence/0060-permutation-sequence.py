class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list (range(1,n+1))
        fact = [1] * n 
        for i in range(1,n):
            fact[i] =fact [i-1] * i

        k -= 1
        res = []

        for i in range(n-1,-1,-1):
            idx = k // fact[i]
            res.append(str(nums.pop(idx)))
            k %= fact[i]

        return "".join(res)
        