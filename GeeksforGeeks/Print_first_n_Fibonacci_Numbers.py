class Solution:
    def printFibb(self,n):
        a=1
        b=1
        l=[a,b]
        if n==1:
            return [1]
        else:
            for i in range(2,n):
                c=a+b
                l.append(c)
                a=b
                b=c
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends
