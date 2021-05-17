class PowerSet:
    def __init__(self):
        pass

    def powerset(self, array, idx = None):
        if idx == None:
            idx = len(array) - 1
        elif idx < 0:
            return [[]]
        ele = array[idx]
        # print(ele)
        subsets = self.powerset(array, idx-1)
        # print(subsets)
        for i in range(len(subsets)):
            currSet = subsets[i]
            subsets.append(currSet + [ele])

        return subsets