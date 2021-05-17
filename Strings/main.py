# Imports
from Easy.Pallendrone import Pallendrone
from Easy.CaesarCipher import CaesarCipher
from Easy.RunLengthEncoding import RunLengthEncoding

from Medium.LongestPalindrome import LongestPalindrome
from Medium.Combos import Combos

# Vars (instances of the classes)
paller = Pallendrone()
caesarCipher = CaesarCipher()
run = RunLengthEncoding

# Pre-Script
def prescript():
    pass


prescript()


# Main Function
def main():
    print("Palindrome : ")
    Pallendrone().check("abcdcba")

    print("\n")

    print("Caesar Cipher Encryptor : ")
    CaesarCipher().caesarCipherEncryptor("ABCK", 9)

    print("\n")

    print("Run Length Encoding : ")
    RunLengthEncoding().getrunlengthalgo("aaa")

    print("\n")

    # □◯△♢❖
    print("Combos : ")
    Combos().getCombos("abab")

    print("\n")

    print("Longest Palindrome")
    LongestPalindrome().longestPalindromicSubstring("abaxyzzyxf")

# Runnable
if __name__ == '__main__':
    main()
