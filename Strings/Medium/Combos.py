from itertools import combinations

class Combos:
    def __init__(self):
        pass

    def getCombos(self, combo_string):

        combo_string_list = list(combo_string)

        filter_list = []
        for i in range(1, len(combo_string_list)):
            filter_list.append(list(combinations(combo_string_list, i)))

        final_list = []

        for i in range(len(filter_list)):
            level = []
            for j in range(len(filter_list[i])):
                str = ""
                for k in filter_list[i][j]:
                    str += k

                level.append(str)

            final_list.append(level)

        final_list.append([combo_string])

        print(f"Combo String : {combo_string}")
        print(f"Combos : {final_list}")

    def getCombosList(self, combo_string):

        combo_string_list = list(combo_string)

        filter_list = []
        for i in range(1, len(combo_string_list)):
            filter_list.append(list(combinations(combo_string_list, i)))

        final_list = []

        for i in range(len(filter_list)):
            level = []
            for j in range(len(filter_list[i])):
                str = ""
                for k in filter_list[i][j]:
                    str += k

                level.append(str)

            final_list.append(level)

        final_list.append([combo_string])

        return final_list