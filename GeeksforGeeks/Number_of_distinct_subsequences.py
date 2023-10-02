class Solution:
    def distinctSubsequences(self, s):
        mod = 1000000007
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
     
        mp = {}
        for i in range(1, n + 1):
            ch = s[i - 1]
            dp[i] = (2 * dp[i - 1]) % mod
            if ch in mp:
                index = mp[ch]
                dp[i] = (dp[i] - dp[index - 1] + mod) % mod
            mp[ch] = i
     
        return dp[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)

# } Driver Code Ends
