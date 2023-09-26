class Solution:
    def fourSum(self, arr, k):
        if len(arr) < 4:
            return []
        
        else:
            ans=[]
            n=len(arr)
            arr.sort()
            for i in range(0,n-3):
                if i > 0 and arr[i]==arr[i-1]:  continue
                for j in range(i+1,n-2):
                    if j >i+1 and arr[j]==arr[j-1]:   continue
                    low,high=j+1,n-1
                    while(low<high):
                        sum=arr[i]+arr[j]+arr[low]+arr[high]
                        if sum == k:
                            ans.append([arr[i],arr[j],arr[low],arr[high]])
                            a,b=arr[low],arr[high]
                            while low<high and arr[low] == a:
                                low+=1
                            while low<high and arr[high] == b:
                                high-=1
                        elif sum<k:
                            low+=1
                        else:
                            high-=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
# } Driver Code Ends
