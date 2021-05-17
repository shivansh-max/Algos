class WaterfallStream:
    def __init__(self):
        pass

    def waterfallStreams(self, array, source):
        rowAbove = array[0][:]

        rowAbove[source]=-1

        for row in range(1, len(array)):
            currentRow = array[row][:]

            for idx in range(len(rowAbove)):
                valueAbove = rowAbove[idx]

                hasWaterAbove = valueAbove < 0
                hasBlock = currentRow[idx] == 1

                if not hasWaterAbove:
                    continue

                if not hasBlock:
                    currentRow[idx] += valueAbove
                    continue

                splitWater = valueAbove / 2

                rightIndex = idx
                while rightIndex + 1 < len(rowAbove):
                    rightIndex += 1

                    if rowAbove[rightIndex] == 1:
                        break

                    if currentRow[rightIndex] != 1:
                        currentRow[rightIndex] += splitWater
                        break

                leftIndex = idx
                while leftIndex - 1 >= 0:
                    leftIndex -= 1

                    if rowAbove[leftIndex] == 1:
                        break

                    if currentRow[leftIndex] != 1:
                        currentRow[leftIndex] += splitWater
                        break
                    



            rowAbove = currentRow

        final = list(map(lambda num: num * -100, rowAbove))

        print(f"Array : {array}")
        print(f"Final Percentages: {final}")
