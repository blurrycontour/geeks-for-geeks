# https://practice.geeksforgeeks.org/problems/binary-tree-to-bst/1

from collections import deque
from typing import List

class Solution:
    def inOrderTraverse(self, root, values:List[int], write=False):
        if root is None:
            return
        self.inOrderTraverse(root.left, values, write)
        if write: # set
            root.data = values.pop()
        else: # get
            values.append(root.data)
        self.inOrderTraverse(root.right, values, write)

    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST(self, root):
        values = []
        self.inOrderTraverse(root, values, False)
        values.sort(reverse=True)
        self.inOrderTraverse(root, values, True)
        return root

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

# Function to print in order
def printInorder(root): 
    if root is None: 
        return
    printInorder(root.left) 
    print (root.data, end=' ')  
    printInorder(root.right) 


if __name__ == "__main__":
    cases = [
        '1 2 3', #
        '1 2 3 4', #
    ]

    for c in cases:
        s = Solution()
        root = buildTree(c)
        s.binaryTreeToBST(root)
        printInorder(root)
        print()
