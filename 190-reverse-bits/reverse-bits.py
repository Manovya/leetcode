class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(32):
            bit = (n>>i) & 1
            r = r | (bit<<(31-i))
        return r


        