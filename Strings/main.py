# Imports
from Pallendrone import Pallendrone
from CaesarCipher import CaesarCipher
from RunLengthEncoding import RunLengthEncoding

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
    # print("Palindrome : ")
    # Pallendrone().check("abcdcba")
    #
    # print("\n")
    #
    # print("Caesar Cipher Encryptor : ")
    # CaesarCipher().caesarCipherEncryptor("ABCK", 9)

    print("\n")

    print("Run Length Encoding : ")
    RunLengthEncoding().encode("aAsSSSSdDDffffRRRR")



# Runnable
if __name__ == '__main__':
    main()
