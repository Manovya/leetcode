class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        r = 0
        n=start^goal
        while n:
            r += n&1
            n= n>>1
        return r


        