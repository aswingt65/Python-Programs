class Solution:
    def perfectSum(self, arr, n, sum):
        dp = [[ 0 for j in range(sum+1)] for i in range(n+1)]
        MOD = int(1e9) + 7
        for i in range(n+1):
            for j in range(sum+1):
                if i == 0 :
                    dp[i][j] = 0
                if j == 0 and i == 0:
                    dp[i][j] = 1
                else:
                    if arr[i-1] <= j:
                        dp[i][j] = (dp[i-1][j-arr[i-1]] + dp[i-1][j]) % MOD
                    else:
                        dp[i][j] = dp[i-1][j]
        return dp[n][sum]   

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends
