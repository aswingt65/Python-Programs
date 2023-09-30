def booleanMatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_flag = [False] * rows
    col_flag = [False] * cols
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                row_flag[i] = True
                col_flag[j] = True
                
    for i in range(rows):
        for j in range(cols):
            if row_flag[i] or col_flag[j]:
                matrix[i][j] = 1
                
    return matrix

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()

# } Driver Code Ends
