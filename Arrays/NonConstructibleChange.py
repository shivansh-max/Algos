class NonConstructibleChange:
    def __init__(self):
        pass

    def calculate(self, coins):
        coins.sort()


        print(f"Coins : {coins}")

        count = 0

        for coin in coins:
            if coin > count + 1:
                print(f"Non constructable change : {count + 1}")
                return count + 1

            count += coin

        print(f"Non constructable change : {count+1}")

        return count + 1