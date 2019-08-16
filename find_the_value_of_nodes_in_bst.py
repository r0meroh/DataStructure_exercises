"""
In this exercise, a function is created to traverse through a tree
and return the sum of all the nodes
"""

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