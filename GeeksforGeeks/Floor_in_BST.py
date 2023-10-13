class Solution:
    def floor(self, root, x):
        if(root):
            s=Solution()
            if (root.data)==x:
                return root.data
            elif(root.data>x):
                return s.floor(root.left,x)
            else:
                a=root.data
                return max(a,s.floor(root.right,x))
        else:
            return -1

#{ 
 # Driver Code Starts

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))
# } Driver Code Ends
