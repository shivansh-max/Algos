class productSum:
    def __init__(self):
        pass

    def productSum(self, array, multi = 1):
        sum = 0

        for ele in array:
            if type(ele) == list:
                sum += self.productSum(ele, multi+1)
            else :
                sum += ele

        return sum*multi
