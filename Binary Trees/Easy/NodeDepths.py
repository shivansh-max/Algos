class NodeDepths:
    def __init__(self):
        pass

    def calculate(self, tree, sumOfNodeDepth = 0, itteration = 0):
        if tree is None:
            return 0
        return sumOfNodeDepth + self.calculate(tree.left, sumOfNodeDepth + 1) + self.calculate(tree.right, sumOfNodeDepth + 1)