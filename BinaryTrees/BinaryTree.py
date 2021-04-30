class BinaryTree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

    def insert(self, data):
        if not self.data:
            self.data = BinaryTree(data)

        q = []
        q.append(self)

        while (len(q)):
            temp = q[0]
            q.pop(0)

            if (not temp.left):
                temp.left = BinaryTree(data)
                break
            else:
                q.append(temp.left)

            if (not temp.right):
                temp.right = BinaryTree(data)
                break
            else:
                q.append(temp.right)

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
