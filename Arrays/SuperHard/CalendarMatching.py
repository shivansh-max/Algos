class ClanderMathching:
    def __init__(self):
        pass

    def calendarMatching(self, employee_one_calendar, employee_one_daily_bounds, employee_two_calendar,
                         employee_two_daily_bounds, meetingDuration):
        updateCal1 = self.updateCalendar(employee_one_calendar, employee_one_daily_bounds)
        updateCal2 = self.updateCalendar(employee_two_calendar, employee_two_daily_bounds)

        mergedCalendar = self.mergeCalendar(updateCal1, updateCal2)
        flatten = self.flatten(mergedCalendar)

        print(f"Cals : \nONE ~> {employee_one_calendar}\nTWO ~> {employee_two_calendar}")
        print(f"BOUNDS : \nONE ~> {employee_one_daily_bounds}\nTWO ~> {employee_two_daily_bounds}")
        print(f"Meet Duration : {meetingDuration}")
        print(f"Possible plots : {self.getMatchingAvailabilities(flatten, meetingDuration)}")

    def flatten(self, calender):
        flattened = [calender[0][:]]
        for i in range(1, len(calender)):
            currMeetingStart, currMeetingEnd = calender[i]
            prevMeeringStart, prevMeeringEnd = flattened[-1]
            if prevMeeringEnd >= currMeetingStart:
                newPrevMeeting = [prevMeeringStart, max(prevMeeringEnd, currMeetingEnd)]
                flattened[-1] = newPrevMeeting
            else:
                flattened.append(calender[i])
        return flattened

    def mergeCalendar(self, calender1, calender2):
        merged = []
        i, j = 0, 0
        while i < len(calender1) and j < len(calender2):
            meeting1, meeting2 = calender1[i], calender2[j]
            if meeting1[0] < meeting2[0]:
                merged.append(meeting1)
                i += 1
            else:
                merged.append(meeting2)
                j += 1

        if i < len(calender1):
            merged.extend(calender1[i:])
        if j < len(calender2):
            merged.extend(calender2[j:])
        return merged

    def getMatchingAvailabilities(self, calender, meetingDuration):
        availabilities = []
        for i in range(1, len(calender)):
            start = calender[i - 1][1]
            end = calender[i][0]
            duration = end - start
            if duration >= meetingDuration:
                availabilities.append([start, end])
        return list(map(lambda m: [self.minuitesToTime(m[0]), self.minuitesToTime(m[1])], availabilities))

    def minuitesToTime(self, minuites):
        hours = minuites // 60
        mins = minuites % 60
        minsStr = "0" + str(mins) if mins < 10 else str(mins)
        return "{}:{}".format(str(hours), minsStr)

    def updateCalendar(self, calendar, dailyBounds):
        updatedCal = []
        updatedCal.append(["0:00", dailyBounds[0]])
        updatedCal.extend(calendar)
        updatedCal.append([dailyBounds[1], "23:59"])
        return list(map(lambda m: [self.timeToMinuites(m[0]), self.timeToMinuites(m[1])], updatedCal))

    def timeToMinuites(self, time):
        hour, mins = list(map(int, time.split(":")))
        return hour * 60 + mins

