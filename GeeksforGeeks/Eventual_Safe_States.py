from typing import List

class Solution:    
    def eventualSafeNodes(self, V: int, adj: List[List[int]]) -> List[int]:
        def is_safe(node):
            if node in safe:
                return True
            if node in visited:
                return False

            visited.add(node)
            for neighbor in adj[node]:
                if not is_safe(neighbor):
                    return False

            visited.remove(node)
            safe.add(node)
            return True

        safe = set()
        visited = set()

        for node in range(V):
            is_safe(node)

        return sorted(list(safe))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends
