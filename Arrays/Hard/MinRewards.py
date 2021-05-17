class MinRewards:
    def __init__(self):
        pass

    def minRewards(self, scores):
        rewards = [1 for _ in scores]

        for i in range(1, len(scores)):
            if scores[i] > scores[i-1]:
                rewards[i] = rewards[i-1]+1
        for i in reversed((range(len(scores)-1))):
            if scores[i] > scores[i+1]:
                rewards[i] = max(rewards[i], rewards[ i + 1 ] + 1)

        print(f"Scores : {scores}")
        print(f"Sum Of Minimum Candies : {sum(rewards)}")