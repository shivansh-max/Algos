class FindSumWithGoalNumber:
    def __init__(self):
        pass

    def findSumWithGoalNumber(self, goalNumber, array):

        found_numbers = []

        print(f"Array : {array}")

        found_numbers = []

        for i in array:

            diff = goalNumber - i

            if i != diff:
                if diff in array:
                    found_numbers.append(i)
                    found_numbers.append(diff)
                    array.pop(array.index(i))
                    array.remove(diff)

                return found_numbers

        print(f"Goal Number : {goalNumber}")
        print(f"Found Numbers {found_numbers}")
