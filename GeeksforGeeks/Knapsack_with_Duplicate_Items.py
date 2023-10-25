class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [[0] * (W + 1) for i in range(N)]
        
        for t in range(W + 1):
            dp[0][t] = (t // wt[0]) * val[0]
            
        for i in range(1, N):
            for j in range(W + 1):
                nottake = 0 + dp[i - 1][j]
                
                take = 0
                if wt[i] <= j:
                    take = val[i] + dp[i][j - wt[i]]
                    
                dp[i][j] = max(take, nottake)
                
        return dp[N-1][W]

#{ 
 # Driver Code Starts

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends
