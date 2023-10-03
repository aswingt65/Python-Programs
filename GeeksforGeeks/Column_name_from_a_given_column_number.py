class Solution:
    def colName (self, n):
        arr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        str=''
        while n > 0:
            s = (n-1) % 26
            str=arr[s]+str
            n = (n-1)//26
        return str

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends
