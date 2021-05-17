class FirstDuplicateNumber(object):
    def __init__(self):
        pass

    def firstDuplicateValue(self, array):
        if len(array) == 0:
            return -1

        foundNums = []
        for i in array:
            if i not in foundNums:
                foundNums.append(i)
            else:
                print(f"Array : {array}")
                print(f"First Duplicate Value : {i}")
                break
