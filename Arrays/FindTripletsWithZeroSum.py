# Given an array of integers. Check whether it contains a triplet that sums up to zero.

class FindTripletsWithZeroSum:
    def __init__(self):
        pass

    def findTripletsWithZeroSumChecker(self, array):
        hasTripletsWithZeroSum = False

        print(f"Array : {array}")

        for i in range(0, len(array) - 2):
            for j in range(i + 1, len(array) - 1):
                for k in range(j + 1, len(array)):
                    if ((array[i] + array[j] + array[k]) == 0):
                        print("Result : True")
                        return True

        print("Result : False")
        return False
