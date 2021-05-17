
class MergeOverlappingIntervals:
    def __init__(self):
        pass

    def mergeOverlappingIntervals(self, intervals):
        sortedIntervals = sorted(intervals, key=lambda x:x[0])

        mergeInterval = []
        currentInterval = sortedIntervals[0]
        mergeInterval.append(currentInterval)

        for next in sortedIntervals:
            _, currentIntervalEnd = currentInterval
            nextStart , nextIntervalEnd = next

            if currentIntervalEnd >= nextStart:
                currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)

            else:
                currentInterval = next
                mergeInterval.append(currentInterval)

        print(f"Intervals : {intervals}")
        print(f"Merged Intervals : {mergeInterval}")
        return mergeInterval



