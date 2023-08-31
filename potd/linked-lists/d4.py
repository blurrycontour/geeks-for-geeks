# https://practice.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self, head):
        result = None
        i = head
        rh = result
        while i.next != None:
            is_valid = True
            j = i.next
            while j != None:
                if i.data < j.data:
                    is_valid = False
                    break
                j = j.next

            if is_valid:
                if rh:
                    rh.next = Node(i.data)
                    rh = rh.next
                else:
                    result = Node(i.data)
                    rh = result

            i = i.next

        # Last node
        if result:
            if i.data <= rh.data:
                rh.next = Node(i.data)
        else:
            result = Node(i.data)
        
        return result


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
        '14 10 5 11 2', # 14 11 2
        '14 10 5 10 2', # 14 10 10 2
        '12 15 10 11 5 6 2 3', # 15 11 6 3
        '10 20 30 40 50 60', # 60
    ]
    
    s = Solution()

    for c in cases:
        l = LinkedList()
        l.appendList(list(map(int, c.strip().split())))
        l.head=s.compute(l.head)
        l.printList()
