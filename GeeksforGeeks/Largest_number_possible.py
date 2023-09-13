class Solution:
    def findLargest(self, N, S):
        a=""
        if S==0 and N>1:
            return "-1"
        if N*9<S:
            return "-1"
        for i in range(N):
            if S>=9:
                a=a+str(9)
                S=S-9
            else:
                a=a+str(S)
                S=S-S
        return a   

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends
