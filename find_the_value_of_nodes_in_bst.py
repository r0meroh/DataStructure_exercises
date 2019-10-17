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
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)

def pre_order(root):
    if not root:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)





class BST_soulution(object):
    def sum_BST(self,root,Left, Right):
       # function to calculate sum
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
        print(" sum is ", self.sum)



my_root = node(5)
insert(my_root, node(8))
insert(my_root, node(9))
insert(my_root, node(2))
insert(my_root, node(1))

print('print tree in order')
in_order(my_root)
print(" \n\n")
print('print tree in "pre-order"')
pre_order(my_root)

print("\n\n")
print('printing value of total nodes in a BST')
tree = BST_soulution()
tree.sum_BST(5, 9, 8)

