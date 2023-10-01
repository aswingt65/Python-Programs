class Solution:
    def BoundaryTraversal(self,matrix, m, n):
        k = 4
        l = 4 * (m + n - 1) if min(m, n) > 1 else max(m, n)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = 0, -1
        res = []
        for d in range(k):
            for i in range(n):
                x += dx[d % 4]
                y += dy[d % 4]
                res.append(matrix[x][y])
            m, n = n, m - 1
        return res[:l]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
