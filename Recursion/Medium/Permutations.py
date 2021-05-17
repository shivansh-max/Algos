class Permutations:
    def __init__(self):
        pass

    def getPermutations(self, permutation_array):
        permutation_array_pers = []
        self.getPermutationsHelper(0, permutation_array, permutation_array_pers)
        return permutation_array_pers

    def getPermutationsHelper(self, i, array, permutations):
        if i == len(array) - 1:
            permutations.append(array[:])
        else :
            for j in range(i, len(array)):
                self.swap(array, i, j)
                self.getPermutationsHelper(i+1, array, permutations)
                self.swap(array, i, j)

    def swap(self, array, index_1, index_2):
        array[index_1], array[index_2] =  array[index_2], array[index_1]