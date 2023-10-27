class Solution:
    def minimumNumberOfDeletions(self,s):
        length=len(s)
        def lcs(s):
            n=len(s)
            dp=[[0]*(n+1) for i in range(n+1)]
            rev=s[::-1]
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if s[i-1]==rev[j-1]:
                        dp[i][j]=1+dp[i-1][j-1]
                    else:
                        dp[i][j]=max(dp[i][j-1],dp[i-1][j])
            return dp[n][n]
        return length-lcs(s)

#{ 
 # Driver Code Starts

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends
