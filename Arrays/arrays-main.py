# Imports
from Easy.ValidateSubsequence import isValidSubsequenceChecker
from Easy.SortedSquaredArray import SortedSquaredArray
from Easy.NonConstructibleChange import NonConstructibleChange
from Easy.SortedSquaredArray import SortedSquaredArray
from Easy.TournamentChampion import Tournament
from Easy.ValidateSubSequenceForStrings import ValidateSubForString

from Medium.ArraysOfProducts import arrayOfProducts
from Medium.FindSumWithGoalNumber import FindSumWithGoalNumber
from Medium.FindTripletsWithZeroSum import FindTripletsWithZeroSum
from Medium.FirstDuplicateNumber import FirstDuplicateNumber
from Medium.LongestPeak import LongestPeak
from Medium.mergeOverlappingIntervals import MergeOverlappingIntervals
from Medium.MonotonicArray import MonotonicArray
from Medium.MoveElementToEnd import MoveElementToEnd
from Medium.SmallestDifference import SmallestDifference
from Medium.spiralConverter import SpiralConverter

from Hard.largestRange import LargestRange
from Hard.SubArraySort import SubArraySort
from Hard.ZigZagTransverse import ZigZagTransverse
from Hard.MinRewards import MinRewards

from SuperHard.apartmentHunting import ApartmentHunting
from SuperHard.WaterfallStream import WaterfallStream
from SuperHard.CalendarMatching import ClanderMathching

# Vars
validateSubForString = ValidateSubForString()
validSubCheck = isValidSubsequenceChecker()
nonCosChange = NonConstructibleChange()
torunament = Tournament()
sortedSquarredArray = SortedSquaredArray()

smallestDiffrence = SmallestDifference()
findTripWithZero = FindTripletsWithZeroSum()
findSumWithGoalNum = FindSumWithGoalNumber()
spiral = SpiralConverter()
arrayOfProducts = arrayOfProducts()
moveElementToEnd = MoveElementToEnd()
longestPeak = LongestPeak()
firstDuplicateNumber = FirstDuplicateNumber()
mergeOverlappingIntervals = MergeOverlappingIntervals()

monotonic = MonotonicArray()
largetrange = LargestRange()
subArraySort = SubArraySort()
zigZag = ZigZagTransverse()
minRewards = MinRewards()

apartment = ApartmentHunting()
calendar = ClanderMathching()
waterfall = WaterfallStream()

def preScript():
    pass


preScript()


# Main
def main():
    # print(validSubCheck.isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
    #
    # print("Is Valid Subsequence Checker : \n")
    # validSubCheck.isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
    #
    # print("\n")
    #
    # print("Find Triplet With Zero Sum : \n")
    # findTripWithZero.findTripletsWithZeroSumChecker([-1, -1, 0])
    #
    # print("\n")
    #
    # print("Is Valid Subsequence Checker for String : \n")
    # validateSubForString.isValidSubsequence("NMEPRO", "MN")
    #
    # print("\n")
    #
    # print("\n")
    #
    # print("Find Sum With Goal Number : \n")
    # findSumWithGoalNum.findSumWithGoalNumber(9, [8, 1, 1, 4, 5])
    #
    # print("\n")
    #
    # print("Tournament : \n")
    # torunament.calculate([
    #     ["AlgoMasters", "FrontPage Freebirds"],
    #     ["Runtime Terror", "Static Startup"],
    #     ["WeC#", "Hypertext Assassins"],
    #     ["AlgoMasters", "WeC#"],
    #     ["Static Startup", "Hypertext Assassins"],
    #     ["Runtime Terror", "FrontPage Freebirds"],
    #     ["AlgoMasters", "Runtime Terror"],
    #     ["Hypertext Assassins", "FrontPage Freebirds"],
    #     ["Static Startup", "WeC#"],
    #     ["AlgoMasters", "Static Startup"],
    #     ["FrontPage Freebirds", "WeC#"],
    #     ["Hypertext Assassins", "Runtime Terror"],
    #     ["AlgoMasters", "Hypertext Assassins"],
    #     ["WeC#", "Runtime Terror"],
    #     ["FrontPage Freebirds", "Static Startup"]
    # ], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])
    #
    # print("\n")
    #
    # print("Smallest Diffrence : \n")
    # smallestDiffrence.smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    #
    # print("\n")
    #
    # print("Non Constructable change : ")
    # nonCosChange.calculate([1, 2, 3, 10, 1])
    #
    # print("\n")
    #
    # print("Spiral : ")
    # arr = [
    #     [1, 2, 3, 4],
    #     [12, 13, 14, 5],
    #     [11, 16, 15, 6],
    #     [10, 9, 8, 7]
    # ]
    # spiraled = []
    # spiral.convert(arr, 0, 0, len(arr), len(arr[0]), spiraled)
    #
    # print("\n")
    #
    # print("Largest Range : \n")
    # largetrange.LargestRange([1, 2, 3, 5, 6, 7, 8, 9])
    #
    # print("\n")
    #
    # print("Apartment Hunting : \n")
    # apartment.find([
    #     {
    #         "gym": False,
    #         "office": True,
    #         "school": True,
    #         "store": False
    #     },
    #     {
    #         "gym": True,
    #         "office": False,
    #         "school": False,
    #         "store": False
    #     },
    #     {
    #         "gym": True,
    #         "office": False,
    #         "school": True,
    #         "store": False
    #     },
    #     {
    #         "gym": False,
    #         "office": False,
    #         "school": True,
    #         "store": False
    #     },
    #     {
    #         "gym": False,
    #         "office": False,
    #         "school": True,
    #         "store": False
    #     },
    #     {
    #         "gym": False,
    #         "office": False,
    #         "school": True,
    #         "store": True
    #     }
    # ], ["gym", "office", "school", "store"])
    #
    # print("\n")
    #
    # print("Sorted Squarred : \n")
    # sortedSquarredArray.square([1, 2, 3, 5, 6, 7, 8, 9])
    #
    # print("\n")
    #
    # print("Move Element To End : ")
    # moveElementToEnd.move([2, 1, 2, 2, 2, 3, 4, 2], 2)
    #
    # print("\n")
    #
    # print("Monotonic : ")
    # monotonic.check([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11])
    #
    # print("\n")
    #
    # print("Longest Peak : ")
    # longestPeak.longestPeak([1, 2, 3, 2, 1])
    #
    # print("\n")
    #
    # print("Array Of Products : ")
    # arrayOfProducts.arrayOfProducts([5, 1, 4, 2])
    #
    # print("\n")
    #
    # print("First Duplicate Number")
    # firstDuplicateNumber.firstDuplicateValue([2,1,5,3,3,2,4])
    #
    # print("\n")
    #
    # mergeOverlappingIntervals.mergeOverlappingIntervals([
    #   [1, 2],
    #   [3, 5],
    #   [4, 7],
    #   [6, 8],
    #   [9, 10]
    # ])
    #
    # print("\n")
    #
    # subArraySort.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
    #
    # print("\n")
    #
    # minRewards.minRewards([8,4,2,1,3,6,7,9,5])
    #
    # print("\n")
    #
    # print("Zig Zag : ")
    # zigZag.zigzagTraverse(
    #     [
    #         [1, 2, 3, 4],
    #         [5, 6, 7, 8],
    #         [9, 10, 11, 12],
    #         [13, 14, 15, 16]
    #     ]
    # )
    #
    # print("\n")
    #
    # print("Calendar")
    # calendar.calendarMatching(
    #     [
    #         ["7:00", "7:45"],
    #         ["8:15", "8:30"],
    #         ["9:00", "10:30"],
    #         ["12:00", "14:00"],
    #         ["14:00", "15:00"],
    #         ["15:15", "15:30"],
    #         ["16:30", "18:30"],
    #         ["20:00", "21:00"]
    #     ],
    #     ["6:30", "22:00"],
    #     [["9:00", "10:00"],
    #      ["11:15", "11:30"],
    #      ["11:45", "17:00"],
    #      ["17:30", "19:00"],
    #      ["20:00", "22:15"]
    #      ],
    #     ["8:00", "22:30"],
    #     30
    # )
    #
    # print("\n")
    #
    print("WaterFall : ")
    waterfall.waterfallStreams([
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
  ], 3)

if __name__ == '__main__':
    main()
