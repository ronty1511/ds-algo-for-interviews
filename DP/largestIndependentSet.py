"""
Given a binary tree, return the size of the largest independent set of nodes such that
no two nodes are connected.
"""

class node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.lis = 0

def largestIndependentSet(root):
    if root == None:
        return 0
    
    if root.lis != 0:
        return root.lis 
    
    if root.left == None and root.right == None:
        root.lis = 1
        return root.lis 
    
    lis_excluding_node = largestIndependentSet(root.left) + largestIndependentSet(root.right)
    lis_including_node = 1

    if root.left != None:
        lis_including_node += (largestIndependentSet(root.left.left)+largestIndependentSet(root.left.right))
    if root.right != None:
        lis_including_node += (largestIndependentSet(root.right.left)+largestIndependentSet(root.right.right))
    root.lis = max(lis_including_node, lis_excluding_node)
    return root.lis

if __name__ == '__main__':
    root = node(20)
    root.left = node(8)
    root.left.left = node(4)
    root.left.right = node(12)
    root.left.right.left = node(10)
    root.left.right.right = node(14)
    root.right = node(22)
    root.right.right = node(25)
    print(largestIndependentSet(root))