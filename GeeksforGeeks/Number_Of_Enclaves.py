from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        queue=[]
        l=[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if (i==0 or i==n-1 or j==0 or j==m-1) and grid[i][j]==1:
                    l[i][j]=1
                    queue.append([i,j])
        
        dir1=[-1,0,1,0]
        dir2=[0,1,0,-1]
        while(len(queue)):
            row=queue[0][0]
            col=queue[0][1]
            queue.pop(0)
            for i in range(4):
                nrow=row+dir1[i]
                ncol=col+dir2[i]
                if nrow>=0 and nrow<n and ncol<m and ncol>=0 and l[nrow][ncol]==0 and grid[nrow][ncol]==1:
                    queue.append([nrow,ncol])
                    l[nrow][ncol]=1
        
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and l[i][j]==0:
                    count+=1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends
