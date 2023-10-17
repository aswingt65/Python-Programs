class Solution:
    def depth_first_search(self, current_vertex, is_visited, graph, num_vertices):
        is_visited[current_vertex] = 1  
        for i in range(num_vertices):
            if i != current_vertex and graph[current_vertex][i] and not is_visited[i]:
                self.depth_first_search(i, is_visited, graph, num_vertices)

    def transitiveClosure(self, num_vertices, graph):
        transitive_closure = []  
        for i in range(num_vertices):
            visited = [0] * num_vertices 
            self.depth_first_search(i, visited, graph, num_vertices)
            transitive_closure.append(visited) 
        return transitive_closure

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        graph = []
        for i in range(0,N):
            graph.append([int(j) for j in input().split()])
        ob = Solution()
        ans = ob.transitiveClosure(N, graph)
        for i in range(N):
            for j in range(N):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends
