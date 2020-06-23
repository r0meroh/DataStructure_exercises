# in this exercise a single linked list is created and duplicates are deleted

# node class
class Node:
    # node constructor
    def __init__(self, name = None, next = None, data = None):
        # parameters for object are set to none unless stated otherwise
        self.name = name
        self.next  = next
        self.data = data

    # to string method, prints out the node's contents whenever a node is called by name
    def __str__(self):
        return "This Node's name is {} and it's next pointer is {}, the data inside is {}."\
            .format(self.name, self.next,self.data)


# linked list object
class linked_List:
    # constructor
    def __init__(self,  size = 0):
        self.size = size
        self.head = None
        self.current = None

    def getSize(self):
        return self.size

    # add a node to the list 'increase the size of the list'
    def add_Node(self, node):

        if node == None:
            print('No node was passed through')
            raise Exception('invalid entry')

        if self.size == 0 and node != None:
            self.head = node
            self.current = node

        elif self.size != 0 and node != None:

            self.current = node
            self.size += 1



    def print_list(self):
        for nodes_in_list in range(self.size):
            print(self.head )






def main():
    # create new node
    hugo = Node('Hugo',None,'35')
    # print node to check toString method
    print(hugo)

    linky = linked_List()
    linky.add_Node(hugo)

    print(linky.getSize())
    linky.print_list()








if __name__ == '__main__':
    main()