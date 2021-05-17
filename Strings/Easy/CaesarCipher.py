class CaesarCipher:
    def __init__(self):
        pass

    def caesarCipherEncryptor(self, s, n):
        n = n%26
        temp = list(s)
        ts = ""
        for i in temp:
            if ord(i) > 64 and ord(i) <= 90:
                diff = ord(i) + n - 90
                if diff > 0:
                    ts += chr(ord('a') + diff - 1)
                else:
                    ts += chr(ord(i) + n)
            if ord(i) > 96 and ord(i) <= 122:
                diff = ord(i) + n - 122
                if diff > 0:
                    ts += chr(ord('A') + diff - 1)
                else:
                    ts += chr(ord(i) + n)
        return ts
