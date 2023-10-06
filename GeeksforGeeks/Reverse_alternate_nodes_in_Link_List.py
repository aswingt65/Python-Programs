class Solution:
    def rearrange(self, head):
        if not head or not head.next or not head.next.next: return head
        first, second, altlast= head, head.next, head.next
        while second and second.next:
            first.next = second.next
            second.next = second.next.next
            first = first.next
            second = second.next
            
        prev = None
        curr = altlast
        
        while curr:
            nxt =curr.next
            curr.next = prev
            prev, curr = curr, nxt
            
        altlast = prev
        first.next = altlast
        return head

#{ 
 # Driver Code Starts
# Node Class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class contains node object
class LinkedList:
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Code execution starts here
if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
            
        Solution().rearrange(llist.head)
        llist.printList()
        t -= 1

# } Driver Code Ends
