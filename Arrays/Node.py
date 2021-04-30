class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def printTreeInOrder(self):
        if self.left:
            self.left.printTreeInOrder()
        print(self.data)
        if self.right:
            self.right.printTreeInOrder()

    def printTreePostOrder(self):
        if self.left:
            self.left.printTreePostOrder()
        if self.right:
            self.right.printTreePostOrder()
        print(self.data)

    def printTreePreOrder(self):
        print(self.data)
        if self.left:
            self.left.printTreePreOrder()
        if self.right:
            self.right.printTreePreOrder()

