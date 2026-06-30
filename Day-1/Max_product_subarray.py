class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pro,m=1,nums[0]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                pro*=nums[j]
                if pro>m:
                    m=pro
            pro=1
        return m