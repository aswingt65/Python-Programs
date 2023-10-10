class Solution:
    def find(self,root,proot,r,p):
        q=[root]
        while(q):
            for i in range(len(q)):
                node=q.pop(0)
                if(node.data==p):
                    r.append(node)
                if(node.left!=None):
                    proot[node.left]=node
                    q.append(node.left)
                if(node.right!=None):
                    proot[node.right]=node
                    q.append(node.right)
   
    def KDistanceNodes(self,root,target,k):
        proot={}
        l=[]
        self.find(root,proot,l,target)
        visit={}
        c=0
        q=[l[0]]
        visit[q[0]]=1
        while(q):
            for i in range(len(q)):
                node=q.pop(0)
                
                if(node.left!=None and  node.left not in visit):
                    visit[node.left]=1
                    q.append(node.left)
                if(node.right!=None and node.right not in visit):
                    visit[node.right]=1
                    q.append(node.right)
                    f=1
                if(node in proot and proot[node] not in visit and proot[node]!=l[0]):
                    visit[proot[node]]=1
                    q.append(proot[node])
            c=c+1
            if(c==k):
                break
        ans=[]
        for i in q:
            ans.append(i.data)
        return sorted(ans)

#{ 
 # Driver Code Starts

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

if __name__ == "__main__":
    x = Solution()
    t = int(input())
    for _ in range(t):
        line = input()
        target=int(input())
        k=int(input())

        root = buildTree(line)
        res = x.KDistanceNodes(root,target,k)
        
        for i in res:
            print(i, end=' ')
        print()

# } Driver Code Ends
