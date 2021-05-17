class SubArraySort:
    def __init__(self):
        pass

    def subarraySort(self, array=[]):
        temp = []
        for i in array:
            temp.append(i)

        temp.sort()

        flag = True

        for i in range(len(array)):
            if array[i] != temp[i]:
                flag=False
                break


        if flag:
            var = [-1,-1]
            print(f"Array : {array}")
            print(temp)
            print(f"Inexes of shortest sub array : {var}")
            return

        array_sorted = temp

        unsorted_sub_array_indexs = []
        for forward_index in range(len(array)):
            if array[forward_index] != array_sorted[forward_index]:
                unsorted_sub_array_indexs.append(forward_index)
                break

        for backword_index in range(len(array) - 1, -1, -1):
            if array[backword_index] != array_sorted[backword_index]:
                unsorted_sub_array_indexs.append(backword_index)
                break

        print(f"Array : {array}")
        print(f"Inexes of shortest sub array : {unsorted_sub_array_indexs}")







