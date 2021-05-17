class LongestPeak:
    def __init__(self):
        pass

    def longestPeak(self, array):
        if array == []:
            return 0

        if len(array) == 1:
            return 1

        lengths = []

        for i in range(len(array)):
            status = True
            length = 1
            direction = True
            if i != len(array) - 1:
                if array[i] < array[i + 1]:
                    for j in range(i + 1, len(array)):
                        if status == False:
                            lengths.append(length)
                            break
                        if direction == True:
                            if j != len(array) - 1:
                                if array[j] < array[j + 1]:
                                    length += 1
                                elif array[j] > array[j + 1]:
                                    direction = False
                                    length += 1
                                else:
                                    status = False
                        else:
                            if j != len(array) - 1:
                                if array[j] > array[j + 1]:
                                    direction = False
                                    length += 1
                                elif array[j] < array[j + 1]:
                                    status = False
                                else:
                                    status = False
                    if status == True:
                        lengths.append(length)

        print(f"Array : {array}")
        print(f"Largest : {self.largest(lengths) + 1}")
        self.largest(lengths)

    def largest(self, arr):
        n = len(arr)

        max = arr[0]

        for i in range(1, n):
            if arr[i] > max:
                max = arr[i]

        return max
