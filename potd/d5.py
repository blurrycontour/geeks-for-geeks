'''
	Your task is to remove duplicates from given 
	sorted linked list.
	
	Function Arguments: head (head of the given linked list) 
	Return Type: none, just remove the duplicates from the list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    prev = head
    current = head.next
    while current != None:
        if current.data == prev.data:
            prev.next = current.next
        else:
            prev = prev.next
        current = current.next


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
        '2 2 4 5', # 2 4 5
        '2 2 2 2 2', # 2
        '2 2 4 4 4 7 7 9', # 2 4 7 9
        '8', # 8
    ]
    
    for c in cases:
        l = LinkedList()
        l.appendList(list(map(int, c.strip().split())))
        removeDuplicates(l.head)
        l.printList()
