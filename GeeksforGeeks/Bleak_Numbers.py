class Solution:
    def is_bleak(self, n):
        # Code here
        def count_set_bit(num):
            ans=0
            while(num>0):
                ans+=(num & 1)
                num=num>>1
            return ans;
            
        for i in range(n-30,n+1):
            if i + count_set_bit(i)==n:
                return 0
        return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_bleak(n)
		print(ans)

# } Driver Code Ends
