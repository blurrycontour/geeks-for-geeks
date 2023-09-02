# https://practice.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1

from collections import deque

class Solution:
    # Return True if the given trees are isomotphic. Else return False.
    def isIsomorphic(self, root1, root2) -> bool:

        if root1 is None and root2 is None:
            return True
        
        if root1.data != root2.data:
            return False

        isometric = True

        data1 = [None, None]
        if root1.left:
            data1[0] = root1.left.data
        if root1.right:
            data1[1] = root1.right.data

        data2 = [None, None]
        if root2.left:
            data2[0] = root2.left.data
        if root2.right:
            data2[1] = root2.right.data

        if data1 == data2 and data1 == data2[::-1]:
            isometric *= self.isIsomorphic(root1.left, root2.left) + self.isIsomorphic(root1.left, root2.right)
            isometric *= self.isIsomorphic(root1.right, root2.right) + self.isIsomorphic(root1.right, root2.left)
        elif data1 == data2:
            isometric *= self.isIsomorphic(root1.left, root2.left)
            isometric *= self.isIsomorphic(root1.right, root2.right)
        elif data1 == data2[::-1]:
            isometric *= self.isIsomorphic(root1.left, root2.right)
            isometric *= self.isIsomorphic(root1.right, root2.left)
        else:
            return False

        return isometric


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
        ('1 2 3 4', '1 3 2 4'), # No
        ('1 2 3 4', '1 3 2 N N N 4'), # Yes
        ('1', '1'), # Yes
        ('1', '2'), # No
        ('4 6 6 N 8 5 7 N 7 4 8', '4 6 6 7 5 8 N N N 8 4 7') # Yes
    ]

    for c in cases:
        s = Solution()
        root1 = buildTree(c[0])
        root2 = buildTree(c[1])
        if s.isIsomorphic(root1, root2):
            print('Yes')
        else:
            print('No')
