from Node import Node

from Easy.FindClosest import FindClosest

MainNode = Node(10)
FindClosest = FindClosest()

def preScript():
    MainNode.insert(5)
    MainNode.insert(2)
    MainNode.insert(5)
    MainNode.insert(10)

    MainNode.insert(15)
    MainNode.insert(13)
    MainNode.insert(22)
    MainNode.insert(4)

preScript()

def main():
    print("Simple Tree :\n")

    print("In Order : ")
    MainNode.printTreeInOrder()
    print("Post Order : ")
    MainNode.printTreePostOrder()
    print("Pre Order : ")
    MainNode.printTreePreOrder()

    print("\n")

    print("Closest Node : ")
    small = {}
    FindClosest.getClosest(MainNode, small, 113)
    print(small)
    print(f"Smallest Node : {min(small, key=small.get)}")



if __name__ == '__main__':
    main()