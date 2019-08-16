"""
In this exercise, a function is created to traverse through a tree
and return the sum of all the nodes
"""

class node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)






class BST_soulution(object):
    def sum_BST(self,root,Left, Right):
        def dfs(node):
            if node:
                if Left <= node.value <= Right:
                    self.sum += node.value
                if Left < node.value:
                    dfs(node.left)
                if node.value < Right:
                    dfs(node.right)


        self.sum = 0
        dfs(root)
        return self.sum