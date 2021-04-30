from BinaryTree import BinaryTree

class BranchAddition:

    def __init__(self):
        pass

    def calculate(self, tree, sums):

        if tree is None:
            return

        newRunningSum = sums + tree.data

        if tree.left == None and tree.right == None:
            sums.append(newRunningSum)
            return

        self.calculate(tree.left, newRunningSum, sums)
        self.calculate(tree.right, newRunningSum, sums)
