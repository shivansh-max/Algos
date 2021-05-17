class SmallestDifference:
    def __init__(self):
        pass

    def checkAro(self, arr1, arr2):
        return len(arr1) >= len(arr2)

    def smallestDifference(self, arrayOne, arrayTwo):
        arrayOne.sort()
        arrayTwo.sort()
        idxOne = 0
        idxTwo = 0
        smallest = float("inf")
        current = float("inf")
        smallestpair = []

        while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
            firstNum = arrayOne[idxOne]
            secondNum = arrayTwo[idxTwo]

            if firstNum < secondNum:
                current = secondNum - firstNum
                idxOne += 1
            elif secondNum < firstNum:
                current = firstNum - secondNum
                idxTwo += 1
            else:
                return [firstNum, secondNum]
            if smallest > current:
                smallest = current
                smallestpair = [firstNum, secondNum]

        print(f"Array One Difference : {arrayOne}")
        print(f"Array Two Difference : {arrayTwo}")
        print(f"Smallest Difference : {current}")
        print(f"Numbers : {smallestpair}")
