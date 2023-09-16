class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        mod=10**9+7
        list=[1,2,4]
        if n<=len(list):
            return list[n-1]
        for i in range(3,n):
            s=list[i-3]+list[i-1]+list[i-2]
            list.append(s%mod)
        return list[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends
