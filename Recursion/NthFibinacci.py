class nthFib:
    def __init__(self):
        pass

    def getNthFib(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else :
            return self.getNthFib(n-1) + self.getNthFib(n-2)
