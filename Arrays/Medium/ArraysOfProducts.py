class arrayOfProducts:
    def __init__(self):
        pass

    def arrayOfProducts(self, array):
        products = []

        for i in range(len(array)):
            duplicate = array.copy()
            duplicate.pop(i)
            prod = 1
            for j in duplicate:
                prod *= j
            products.append(prod)

        print(f"Array : {array}")
        print(f"Products : {products}")
