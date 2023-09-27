class Solution:
    def printClosest (self,arr, brr, n, m, x) :     
        i = 0
        j = m-1
        mini = sum(arr) + sum(brr)
        while i < n and j >= 0:
            diff = abs(arr[i]+brr[j] - x)
            if diff <= mini:
                mini = diff
                one = arr[i]
                two = brr[j]
            if arr[i] + brr[j] > x:
                j -= 1
            else:
                i += 1
        return [one, two]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    x = int(input())
    ob = Solution()
    ans = ob.printClosest(arr, brr, n, m, x)
    print(abs(ans[0]+ans[1] - x))
# } Driver Code Ends
