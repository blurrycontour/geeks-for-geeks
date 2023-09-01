# https://practice.geeksforgeeks.org/problems/leaf-under-budget/1

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

from collections import deque

class Solution:
    def isLeaf(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    def min_cumsum(self, array, threshold):
        array = sorted(array)
        budget = 0
        count = 0
        for cost in array:
            budget += cost
            if budget <= threshold:
                count += 1
            else:
                break
        return count

    def getCount(self, root, n):
        leaf_costs = []
        q = deque()
        q.append(root)

        level = 1
        while len(q) > 0:
            for _ in range(len(q)):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)

                if self.isLeaf(q[0]):
                    leaf_costs.append(level)
                q.popleft()

            level += 1

        return self.min_cumsum(leaf_costs, n)

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
    
 
if __name__=="__main__":
    cases = [
        ('10 8 2 3 N 3 6 N N N 4', 8), # 2
        ('1 2 3 4 5 6 7', 5), # 1
        ('1 2 3 4', 0), # 0
        ('1', 5), # 1
    ]
    
    for c in cases:
        s = Solution()
        root = buildTree(c[0])
        ans = s.getCount(root, c[1])
        print(ans)
