# https://practice.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, k):
    if k == 1:
        return head.next
    
    current = head
    for _ in range(k-2):
        current = current.next
    current.next = current.next.next

    return head

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail =new_node
            return
        self.tail.next=new_node
        self.tail=new_node

    def appendList(self, new_values):
        for x in new_values:
            self.append(x)

    def getNode(self,value): # return node with given value, if not present return None
        curr_node=self.head
        while(curr_node.next and curr_node.data != value):
            curr_node=curr_node.next
        if(curr_node.data==value):
            return curr_node
        else:
            return None

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print(' ')

if __name__ == "__main__":
    cases = [
        ('1 3 4', 3), # 1 3
        ('1 5 2 9', 2), # 1 2 9
        ('1 5 2 9', 1), # 5 2 9
    ]
    
    for c in cases:
        l = LinkedList()
        l.appendList(list(map(int, c[0].strip().split())))
        l.head=delNode(l.head, c[1])
        l.printList()
