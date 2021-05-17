from BinaryTree import BinaryTree

from Easy.BranchAddition import BranchAddition
from Easy.NodeDepths import NodeDepths

tree = BinaryTree(90)
branchAddition = BranchAddition()
nodeDepth = NodeDepths()


def preScript():
    tree.insert(90)
    tree.insert(80)
    tree.insert(70)
    tree.insert(60)
    tree.insert(50)
    tree.insert(40)
    tree.insert(30)
    tree.insert(20)
    tree.insert(10)


preScript()


def main():
    print("Simple BinaryTree (InOrder, PostOrder, PutOrder) : ")
    tree.printTreeInOrder()

    print("\n")

    print("Sums : ")
    sums = []
    branchAddition.calculate(tree, 0, sums)
    print(f"Sums : {sums}")

    print("\n")
    print(type(nodeDepth.calculate(tree, 0)))
    print(f"Node Depth : {nodeDepth.calculate(tree, 0)}")

#

if __name__ == '__main__':
    main()
