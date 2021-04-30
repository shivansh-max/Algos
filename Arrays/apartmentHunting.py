class ApartmentHunting:
    def __init__(self):
        pass

    def find(self, blocks, reqs):

        str = "[\n"
        for i in blocks:
            str += f"{i}"

            if i == len(blocks):
                str += "\n"
            else:
                str += ",\n"
        str += "]"

        matches = {}

        for i in range(len(blocks)):
            matches[i] = 0
            block = blocks[i]
            for j in range(len(reqs)):
                req = reqs[j]
                if block[req]:
                    if j == 0:
                        matches[i] += 1
                    else:
                        matches[i] += 1 / j

        max_key = max(matches, key=matches.get)

        print(f"Blocks : {str}")
        print(f"Scores : {matches}")
        print(f"Reqs : {reqs}")
        print(f"Block : {max_key} contains : {blocks[max_key]}")
