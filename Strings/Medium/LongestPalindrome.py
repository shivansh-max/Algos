from itertools import combinations
from Combos import Combos
from Pallendrone import Pallendrone

combo_creater = Combos()
pallendrome = Pallendrone()

class LongestPalindrome:
    def __init__(self):
        pass

    def longestPalindromicSubstring(self, check_str):
        combos = combo_creater.getCombosList(check_str)

        combos_scores = {}

        for i in combos:
            for j in i:
                if pallendrome.checkAndReturnTrueFalse(j):
                    combos_scores[j] = len(list(j))

        print(f"Check String : {check_str}")
        # print(f"Combos : {combos}")
        # print(f"Combos Scores : {combos_scores}")
        print(f"Longest Combo : {max(combos_scores, key=combos_scores. get)}")



