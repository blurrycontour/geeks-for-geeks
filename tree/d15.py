# https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1

from collections import deque

class Solution:
    def inOrderTraverse(self, root, k, i=0):
        if root is None:
            return i, None

        i, kth = self.inOrderTraverse(root.right, k, i)
        if kth:
            return i, kth

        i += 1
        if i == k:
            kth = root.data
            return i, kth

        i, kth = self.inOrderTraverse(root.left, k, i)
        return i, kth

    # return the Kth largest element in the given BST rooted at 'root'
    def kthLargest(self, root, k):
        return self.inOrderTraverse(root, k, 0)[1]

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


if __name__ == "__main__":
    cases = [
        ('4 2 9', 2), # 4
        ('9 N 10', 1), # 10
        ('5', 1), # 5
    ]

    for c in cases:
        s = Solution()
        root = buildTree(c[0])
        res = s.kthLargest(root, c[1])
        print(res)
