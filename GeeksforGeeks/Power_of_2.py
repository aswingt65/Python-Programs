class Solution:
    def isPowerofTwo(self,n):
        if n==0:
            return 0
        else:
            return ((n & -n)^n == 0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
