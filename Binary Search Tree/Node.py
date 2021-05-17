import sys

sys.setrecursionlimit((10**5 ))


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value != None:
            if data > self.value:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data <= self.value:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.value = Node(data)

    def printTreeInOrder(self):
        if self.left:
            self.left.printTreeInOrder()
        print(self.value)
        if self.right:
            self.right.printTreeInOrder()

    def printTreePostOrder(self):
        if self.left:
            self.left.printTreePostOrder()
        if self.right:
            self.right.printTreePostOrder()
        print(self.value)

    def printTreePreOrder(self):
        print(self.value)
        if self.left:
            self.left.printTreePreOrder()
        if self.right:
            self.right.printTreePreOrder()

