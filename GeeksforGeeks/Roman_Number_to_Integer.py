class Solution:
    def romanToDecimal(self, S): 
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        c=0
        for i in range(1,len(S)):
            cu=S[i]
            pr=S[i-1]
            if(d[pr]>=d[cu]):
                c+=d[pr]
            else:
                c-=d[pr]
        k=S[-1]
        c+=d[k]
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
      
# } Driver Code Ends
