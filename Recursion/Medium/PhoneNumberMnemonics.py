class PhoneNumberMnemonics:
    def __init__(self):
        self.key = {
            "0": ["0"],
            "1": ["1"],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

    def phoneNumberMnemonics(self, phoneNumber):
        curentMenomic = ['0'] * len(phoneNumber)
        found = []

        self.phoneNumberMnemonicsHelper(0, phoneNumber, curentMenomic, found)
        return found

    def phoneNumberMnemonicsHelper(self, index, phoneNumber, curentMenomic, found):
        if index == len(phoneNumber):
            menomic = ''.join(curentMenomic)
            found.append(menomic)
        else:
            digit = phoneNumber[index]
            letters = self.key[digit]
            for letter in letters :
                curentMenomic[index] = letter
                self.phoneNumberMnemonicsHelper(index+1, phoneNumber, curentMenomic, found)
