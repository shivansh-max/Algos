class MonotonicArray:
    def __init__(self):
        pass

    def check(self, array):
        print(f"Array : {array}")
        print(f"Monotonic : {self.checkHelper(array)}")

    def checkHelper(self, array):
        if len(array) < 1:
            return True

        status = True
        asscending = self.firstChck(array)
        for i in range(2, len(array)):
            if status == False:
                break
            if asscending == False:
                if array[i-1] >= array[i]:
                    status = True
                else:
                    status = False
            if asscending == True:
                if array[i - 1] <= array[i]:
                    status = True
                else:
                    status = False
        return status


    def firstChck(self, array):
        index1 = 0
        while array[index1] == array[index1+1]:
            index1 += 1
            if index1 > len(array) - 2 :
                return True

        if array[index1] >= array[index1+1]:
            return False
        elif array[index1] <= array[index1+1]:
            return True