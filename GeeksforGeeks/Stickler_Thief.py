class Solution:  
    def FindMaxSum(self,a, n):
        dp = [0] * n
        dp[0] = a[0]
        dp[1] = max(a[0], a[1])
        for i in range(2, n):
            dp[i] = max(a[i] + dp[i - 2], dp[i - 1])
        return dp[n - 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends
