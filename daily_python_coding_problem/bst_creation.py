class bstNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            print('current node is root')
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = bstNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = bstNode(data)


    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
    # LnR
    def in_order(self):
        elements = []

        if self.left:
            print(self.data)
            elements += self.left.in_order()

        elements.append(self.data)

        if self.right:
            print(self.data)
            elements += self.right.in_order()



        return elements


def build_bst(nodes):
    root = bstNode(nodes[0])

    for x in range(len(nodes)):
        root.add_child(nodes[x])

    return root


if __name__ == '__main__':
    nums = [1,2,11,33,333,4,41,9]

    my_tree = build_bst(nums)
    print(my_tree.in_order())
    print(my_tree.search(333))
