class Solution:
    def nextClosestTime(self, time: str) -> str:
        hour,minute = time.split(':')
        usable = {hour[0], hour[1], minute[0], minute[1]}
        hournunber = int(hour)
        minutenumber = int(minute)
        while True:
            minutenumber = minutenumber + 1
            if minutenumber == 60:
                minutenumber = 0
                hournunber = hournunber + 1
                if hournunber == 24:
                    hournunber = 0
            minutestr =f"{minutenumber:02d}"
            hourstr = f"{hournunber:02d}"
            if minutestr[0] in usable and minutestr[1] in usable and hourstr[0] in usable and hourstr[1] in usable:
                return hourstr + ":" + minutestr


s = Solution()
print(s.nextClosestTime("23:59"))