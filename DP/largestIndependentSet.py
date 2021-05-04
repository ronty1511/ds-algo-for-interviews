"""
    Given a binary tree, return the size of the largest independent set of nodes such that
    no two nodes are connected.

    For any node, if I don't consider the node in my largest set of independent nodes, 
    I can add the count of subsets with subtrees rooted with node.left and node.right.
    Now if I consider the node, I cannot put node.left or node.right as they are directly
    connected. I'll consider root.left.left, root.left.right, root.right.left and 
    root.right.right (obviously only if left and right != None).

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
