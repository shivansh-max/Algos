class SortedSquaredArray:
    def __init__(self):
        pass

    def square(self, array):
        squared = []
        for i in array:
            squared.append(i**2)

        print(f"Array : {array}")
        print(f"Squared Array : {squared}")