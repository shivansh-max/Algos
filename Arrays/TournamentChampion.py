class Tournament:
    def __init__(self):
        pass

    def calculate(self, competitions, scores):
        teams = {}

        for i in range(len(competitions)):
            val = competitions[i]

            print(val[0])

            if val[0] not in teams.keys():
                teams[val[0]] = 0
            if val[1] not in teams.keys():
                teams[val[1]] = 0

            if scores[i] == 1:
                teams[val[0]] += 3
            else:
                teams[val[1]] += 3

        print(f"Competitions : {competitions}")
        print(f"Scores : {scores}")
        print(f"Teams : {teams}")
        print(f"Winner : {max(teams, key=teams.get)}")

