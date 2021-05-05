import collections

class RunLengthEncoding:
    def __init__(self):
        pass

    def encode(self, stringer):
        # stringList = list(stringer)
        #
        # encodedString = ""
        #
        # match_coding = []
        # newReq = True
        # currentItterationString = ""
        # current = 0
        # for i in range(1, len(stringList)):
        #     if newReq:
        #         match_coding.append(f"{current + 1}-{currentItterationString}")
        #         currentItterationString = stringList[i]
        #         current = 0
        #         newReq = False
        #     if stringList[i] == currentItterationString:
        #         current += 1
        #     else:
        #         newReq = True
        # match_coding.append(f"{current + 1}-{currentItterationString}")
        # match_coding.pop(0)
        # for i in match_coding:
        #     currList = i.split("-")
        #     currList[0] = int(currList[0])
        #     curr = currList[0]
        #     while curr > 9:
        #         print(curr > 9)
        #         encodedString += "9" + currList[1]
        #         curr -= 9
        #     encodedString += str(curr) + currList[1]
        #
        # print(f"String: {stringer}")
        # print(f"Matches : {match_coding}")
        # print(f"Encoded Version : {encodedString}")

        seen = set()
        return [x for x in stringer if not (x in seen or seen.add(x))]


    def getrunlengthalgo(self, s):

        print(f"String : {s}")

        temp = collections.Counter(s)
        rtemp = self.encode(s)
        ftemp = ""

        for i in rtemp:
            if temp.get(i) > 9:
                for j in range(int(temp.get(i)) // 9):
                    ftemp += "9" + str(i)
                ftemp += str(int(temp.get(i))%9)
                ftemp += str(i)

            else :
                ftemp += str(temp.get(i))
                ftemp += str(i)

        print(f"Ecoded String : {ftemp}")
        return ftemp
