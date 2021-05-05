class Pallendrone:
    def __init__(self):
        pass

    def reverse(self, reverse_str):
        str_list = list(reverse_str)
        return_str = ""

        for i in range(0, len(str_list)):
            bob = len(str_list) - (i) - 1
            return_str += str_list[bob]

        return return_str

    def check(self, check_str):

        if check_str == self.reverse(check_str):
            print(f"String {check_str} is a palindrome.")
            return

        print(f"String {check_str} is not a palindrome.")

    def checkAndReturnTrueFalse(self, check_str):
        if check_str == self.reverse(check_str):
            return True

        return False