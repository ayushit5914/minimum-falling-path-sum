class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #recursion
        # n=len(matrix)
        # def func(i,j):
        #     if j<0 or j>n-1:
        #         return sys.maxsize
        #     if i==0:
        #         return matrix[i][j]
        #     same=matrix[i][j]+func(i-1,j)
        #     left=matrix[i][j]+func(i-1,j-1)
        #     right=matrix[i][j]+func(i-1,j+1)
        #     return min(same,left,right)
        # ans=func(n-1,0)
        # for i in range(1,n):
        #     ans=min(ans,func(n-1,i))
        # return ans

        #memoization
        # n=len(matrix)
        # dp={}
        # def func(i,j):
        #     if j<0 or j>n-1:
        #         return sys.maxsize
        #     if i==0:
        #         return matrix[i][j]
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     same=matrix[i][j]+func(i-1,j)
        #     left=matrix[i][j]+func(i-1,j-1)
        #     right=matrix[i][j]+func(i-1,j+1)
        #     dp[(i,j)]= min(same,left,right)
        #     return dp[(i,j)]
        # ans=func(n-1,0)
        # for i in range(1,n):
        #     ans=min(ans,func(n-1,i))
        # return ans

        #tabulation
        # n=len(matrix)
        # dp=[([0]*n) for i in range(n)]
        # for j in range(n):
        #     dp[0][j]=matrix[0][j]
        # for i in range(1,n):
        #     for j in range(n):
        #         same=matrix[i][j]+dp[i-1][j]
        #         if j-1>=0:
        #             left=matrix[i][j]+dp[i-1][j-1]
        #         else:
        #             left=sys.maxsize
        #         if j+1<n:
        #             right=matrix[i][j]+dp[i-1][j+1]
        #         else:
        #             right=sys.maxsize
        #         dp[i][j]=min(same,left,right)  
        # return min(dp[n-1])

        #space optimization
        n=len(matrix)
        dp=[0]*n
        for j in range(n):
            dp[j]=matrix[0][j]
        for i in range(1,n):
            temp=[0]*n
            for j in range(n):
                same=matrix[i][j]+dp[j]
                if j-1>=0:
                    left=matrix[i][j]+dp[j-1]
                else:
                    left=sys.maxsize
                if j+1<n:
                    right=matrix[i][j]+dp[j+1]
                else:
                    right=sys.maxsize
                temp[j]=min(same,left,right)
            dp=temp
        return min(dp)
