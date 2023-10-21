class Solution:
    def sumOfDivisors(self, N):
        if N <= 0:
          return 0
        div_sum = 0
            
        for i in range(1, N + 1):
          k = N // i
          div_sum += i * k
        
        return div_sum

#{ 
 # Driver Code Starts

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
# } Driver Code Ends
