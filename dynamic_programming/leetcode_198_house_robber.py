class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums)==1:
            return nums[0]
        
        dp=[0 for i in range(len(nums))]
        
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        
        if len(dp)==2:
            return dp[1] 
    
        for i in range(2,len(dp)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        
        
        return dp[len(nums)-1]