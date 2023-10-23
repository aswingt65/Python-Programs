class Solution:
    def maxSumIS(self, Arr, n):
        if n==0:
            return 0
        dp = [0] * n
        dp[n - 1] = Arr[n - 1]
         
        for i in reversed(range(n - 1)):
            maxSum = 0
            for j in range(i + 1, n):
                if Arr[j] > Arr[i]:
                    maxSum = max(maxSum, dp[j])
            dp[i] = Arr[i] + maxSum
 
        return max(dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends
