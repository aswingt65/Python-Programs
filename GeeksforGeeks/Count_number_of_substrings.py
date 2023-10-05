class Solution:
    def substrCount (self,s, k):
        return self.solve(s, k) - self.solve(s, k-1)
    
    def solve(self, s, k):
        left = count = 0
        m = dict()
        
        for right in range(len(s)):
            m[s[right]] = m.get(s[right], 0)
            m[s[right]] += 1
            
            while len(m) > k:
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    del m[s[left]]
                
                left += 1
            
            count += right - left + 1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends
