class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        dp=triangle[-1]
        

        n=len(triangle)
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j]=min(dp[j],dp[j+1])+triangle[i][j]
        

        return dp[0]