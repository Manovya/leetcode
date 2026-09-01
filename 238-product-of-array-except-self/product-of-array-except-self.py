class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p=[1]*n
        s= [1]*n
        a=[1]*n
        for i in range(1,n):
            p[i] = p[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            s[i] = s[i+1]*nums[i+1]
        for i in range(n):
            a[i] = p[i]*s[i]
        return a

        