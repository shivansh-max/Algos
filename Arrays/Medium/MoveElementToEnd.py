class MoveElementToEnd:
    def __init__(self):
        pass

    def move(self, arrays, element):
        newArr = []

        ele_amount = 0
        for i in arrays:
            if i != element:
                newArr.append(i)
            else:
                ele_amount += 1
        for i in range(ele_amount):
            newArr.append(element)

        print(f"Arrar : {arrays}")
        print(f"Element : {element}")
        print(f"Moved Array : {newArr}")
