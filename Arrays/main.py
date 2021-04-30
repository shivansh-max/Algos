# Imports
from ValidateSubsequence import isValidSubsequenceChecker
from FindTripletsWithZeroSum import FindTripletsWithZeroSum
from ValidateSubSequenceForStrings import ValidateSubForString
from Node import Node
from FindSumWithGoalNumber import FindSumWithGoalNumber
from TournamentChampion import Tournament
from SmallestDifference import SmallestDifference
from NonConstructibleChange import NonConstructibleChange
from spiralConverter import SpiralConverter
from largestRange import LargestRange
from apartmentHunting import ApartmentHunting

# Vars
validSubCheck = isValidSubsequenceChecker()
findTripWithZero = FindTripletsWithZeroSum()
validateSubForString = ValidateSubForString()
simpleTreeFromScratch = Node(100)
torunament = Tournament()
findSumWithGoalNum = FindSumWithGoalNumber()
smallestDiffrence = SmallestDifference()
nonCosChange = NonConstructibleChange()
spiral = SpiralConverter()
largetrange = LargestRange()
apartment = ApartmentHunting()


def preScript():
    simpleTreeFromScratch.insert(90)
    simpleTreeFromScratch.insert(80)
    simpleTreeFromScratch.insert(70)
    simpleTreeFromScratch.insert(60)
    simpleTreeFromScratch.insert(50)
    simpleTreeFromScratch.insert(40)
    simpleTreeFromScratch.insert(30)
    simpleTreeFromScratch.insert(20)
    simpleTreeFromScratch.insert(10)


preScript()


# Main
def main():
    print(validSubCheck.isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))

    print("Is Valid Subsequence Checker : \n")
    validSubCheck.isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])

    print("\n")

    print("Find Triplet With Zero Sum : \n")
    findTripWithZero.findTripletsWithZeroSumChecker([-1, -1, 0])

    print("\n")

    print("Is Valid Subsequence Checker for String : \n")
    validateSubForString.isValidSubsequence("NMEPRO", "MN")

    print("\n")

    print("Print Trees : \n")
    print("TreeList : [100,90,80,70,60,50,40,30,20,10]\n")
    print("In Order : \n")
    simpleTreeFromScratch.printTreeInOrder()
    print("Post Order : \n")
    simpleTreeFromScratch.printTreePostOrder()
    print("Pre Order : \n")
    simpleTreeFromScratch.printTreePreOrder()

    print("\n")

    print("Find Sum With Goal Number : \n")
    findSumWithGoalNum.findSumWithGoalNumber(9, [8, 1, 1, 4, 5])

    print("\n")

    print("Tournament : \n")
    torunament.calculate([
        ["AlgoMasters", "FrontPage Freebirds"],
        ["Runtime Terror", "Static Startup"],
        ["WeC#", "Hypertext Assassins"],
        ["AlgoMasters", "WeC#"],
        ["Static Startup", "Hypertext Assassins"],
        ["Runtime Terror", "FrontPage Freebirds"],
        ["AlgoMasters", "Runtime Terror"],
        ["Hypertext Assassins", "FrontPage Freebirds"],
        ["Static Startup", "WeC#"],
        ["AlgoMasters", "Static Startup"],
        ["FrontPage Freebirds", "WeC#"],
        ["Hypertext Assassins", "Runtime Terror"],
        ["AlgoMasters", "Hypertext Assassins"],
        ["WeC#", "Runtime Terror"],
        ["FrontPage Freebirds", "Static Startup"]
    ], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])

    print("\n")

    print("Smallest Diffrence : \n")
    smallestDiffrence.smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])

    print("\n")

    print("Non Constructable change : ")
    nonCosChange.calculate([1,2,3,10,1])

    print("\n")

    print("Spiral : ")
    arr = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ]
    spiraled = []
    spiral.convert(arr, 0, 0, len(arr), len(arr[0]), spiraled)

    print("\n")

    print("Largest Range : \n")
    largetrange.LargestRange([1,2,3,5,6,7,8,9])

    print("\n")

    print("Apartment Hunting : \n")
    apartment.find([
    {
      "gym": False,
      "office": True,
      "school": True,
      "store": False
    },
    {
      "gym": True,
      "office": False,
      "school": False,
      "store": False
    },
    {
      "gym": True,
      "office": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "office": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "office": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "office": False,
      "school": True,
      "store": True
    }
  ], ["gym", "office", "school", "store"])


if __name__ == '__main__':
    main()
