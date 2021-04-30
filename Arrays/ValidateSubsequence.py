# Given two arrays of integers write a function that determines whether the second array is a subsequence
# of the firs one


class isValidSubsequenceChecker:
    def __init__(self):
        pass

    def isValidSubsequence(self, array, sequence):

        count = 0

        print(f"Array : {array}")
        print(f"Sequence : {sequence}")

        for i in array:
            if (i == sequence[count]):
                count += 1
                if (count == len(sequence)):
                    print("Result : True")
                    return True

        print("Result : False")
        return False
