class Solution:
    def isLucky(self, n): 
        c=2
        while c<=n:
            if (n%c==0):
                return False
            n=n-n//c
            c+=1
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends
