class FindClosest:

    def __init__(self):
        pass

    def getClosest(self,root, minList, inval):
        if root == None:
            return

        if root.left:
            self.getClosest(root.left, minList, inval)
        minList[root.value] = abs(inval - root.value)
        if root.right:
            self.getClosest(root.right, minList, inval)
