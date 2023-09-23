class Solution:                              
    def equilibriumPoint(self,A, N):
        left = right = 0
        i = 0
        j = N-1
        while i < j :
            if left <= right :
                left += A[i]
                i += 1
            else :
                right += A[j]
                j -= 1
        if left == right :
            return j + 1
        else :
            return -1

#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math
def main():
    T = int(input())
    while(T > 0):

        N = int(input())
        A = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.equilibriumPoint(A, N))
        T -= 1
if __name__ == "__main__":
    main()

# } Driver Code Ends
