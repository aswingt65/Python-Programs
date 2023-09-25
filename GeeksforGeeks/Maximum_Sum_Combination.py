import heapq
class Solution:
    def maxCombinations(self, n, k, a, b):
        a.sort()
        b.sort()
        ans=[]
        hp=[]
        for i in range(n):
            heapq.heappush(hp,[-(a[i]+b[-1]),i,n-1])
        
        while k:
            el,i,j=heapq.heappop(hp)
            ans.append(-el)
            heapq.heappush(hp,[-(a[i]+b[j-1]),i,j-1])
            k-=1
        return ans


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxCombinations(N, K, A, B)
        for val in res:
            print(val, end =' ')
        print()
# } Driver Code Ends
