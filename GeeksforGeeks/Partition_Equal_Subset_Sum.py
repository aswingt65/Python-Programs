class Solution:
    def equalPartition(self, N, arr):
        s = sum(arr)
        if s % 2 != 0:
            return False
        s //= 2
        dp = [False] * (s + 1)
        dp[0] = True
        for item in arr:
            st = set()
            for j in range(item, s + 1):
                if dp[j] == False and dp[j - item] and j - item not in st:
                    dp[j] = True
                    st.add(j)
                if dp[s]:
                    return True
        return False
        
#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends
