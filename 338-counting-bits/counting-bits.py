class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0]*(n+1)
 
        o = 1
        for i in range(1,n+1):
            if o*2 == i:
                o=i
            dp[i]=1+dp[i-o]
        return dp
        