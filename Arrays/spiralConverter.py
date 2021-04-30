class SpiralConverter:
    def __init__(self):
        pass

    def convert(self, array, i, j, m, n, spiraled):

        if (i > m or j > n):
            print(f"Array : {array}")
            print(f"Spiraled : {spiraled}")
            return spiraled

        for p in range(i,n):
            spiraled.append(array[i][p])

        for q in range(i+1, m):
            spiraled.append(array[q][n-1])

        if ((m-1) != i):
            for p in range(n-2, j-1, -1):
                spiraled.append(array[m-1][p])

        if ((n-1) != j):
            for p in range(m-2, i, -1):
                spiraled.append(array[p][j])

        self.convert(array, i+1, j+1, n-1, m-1, spiraled)

