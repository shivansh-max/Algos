class ValidateSubForString:
    def __init__(self):
        pass

    def isValidSubsequence(self, mainstring, checkstring):

        array = list(mainstring)
        sequence = list(checkstring)

        print("Main String")
        print(f"Main String : {mainstring}")
        print(f"Main Array {array} \n")

        print("Check String")
        print(f"Check String : {checkstring}")
        print(f"Check Array : {sequence}\n")


        count = 0

        for i in array:
            if (i == sequence[count]):
                count += 1
                if (count == len(sequence)):
                    print("Result : True")
                    return True

        print("Result : False")
        return False
