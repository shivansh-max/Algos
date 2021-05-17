import numpy as np

class ZigZagTransverse:
    def __init__(self):
        pass

    def zigzagTraverse(self, array):
        height = len(array) - 1
        width = len(array[0]) - 1

        results = []

        row,col = 0,0
        goingDown = True
        while not self.isOutOfBounds(row, col, height, width):
            results.append(array[row][col])
            if goingDown:
                if col == 0 or row == height:
                    goingDown=False
                    if row == height:
                        col += 1
                    else:
                        row += 1
                else:
                    row += 1
                    col -= 1
            else:
                if row == 0 or col == width:
                    goingDown = True
                    if col == width:
                        row += 1
                    else:
                        col += 1
                else:
                    row -= 1
                    col += 1

        print(f"Array : \n{np.array(array)}")
        print(f"Zig Zag Transverse : {results}")

    def isOutOfBounds(self, row, col, height, width):
        return row < 0 or row > height or col < 0 or col > width

