# Imports
from Easy.NthFibinacci import nthFib
from Easy.productSum import productSum

from Medium.Permutations import Permutations
from Medium.PhoneNumberMnemonics import PhoneNumberMnemonics
from Medium.PowerSet import PowerSet

# PreScript
def pre_script():
    pass


# Main Function
def main():
    fibNum = 8
    print("Nth Fibonacci : ")
    print(f"Fibonacci of {fibNum} : {nthFib().getNthFib(fibNumb)}")

    print("\n")

    prodSum = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    print("Product Sum : ")
    print(f"Product Sum Of List {prodSum} : {productSum().productSum(prodSum)}")

    print("\n")

    per = [1,2,3]
    print("Permutations : ")
    print(f"Perumations of Array {per} : {Permutations().getPermutations(per)}")

    print("\n")

    powerArr = [1,2,3,4]
    print("Power Set : ")
    print(f"Power Set of {powerArr} is {PowerSet().powerset(powerArr)}")

    print("\n")

    number = "74482674"
    print("Phone Number Mnemonics : ")
    print(f"Phone Number Mnemonic of number : {number} is {PhoneNumberMnemonics().phoneNumberMnemonics(number)}")
# Runnable
if __name__ == '__main__':
    main()
