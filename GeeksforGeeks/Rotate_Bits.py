class Solution:
    def rotate(self,N,D):
        s = bin(N)
        s = s[2:]
        if(D>16): D %= 16
        adder = '0'*(16-len(s))
        s = adder + s
        res = []
        r_left = s[D:]+s[:D]
        r_right = s[len(s)-D:]+s[:len(s)-D]
        res.append(int(r_left,2))
        res.append(int(r_right,2))
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends
