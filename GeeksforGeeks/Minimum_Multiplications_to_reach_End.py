from typing import List
from collections import deque 

class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        visited = set()
        visited.add(start)
   
        queue = deque([(start, 0)])  

        while queue:
            node, count = queue.popleft()
        
            if node == end:
                return count
       
            for i in arr:
                next_value = (node * i) % 100000
    
                if next_value not in visited:
                    visited.add(next_value)
                    queue.append((next_value, count + 1))
   
        return -1

#Driver code
if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
