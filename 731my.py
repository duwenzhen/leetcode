class MyCalendarTwo1:

    def __init__(self):
        self.dico = {}

    def book(self, start: int, end: int) -> bool:
        for i in range(start, end, 1):
            if i not in self.dico:
                self.dico[i] = 1
            else:
                if self.dico[i] == 2:
                    for j in range(start, i, 1):
                        self.dico[j] = self.dico[j] - 1
                    return False
                self.dico[i] = self.dico[i] + 1
        return True

class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True



myCalendarTwo = MyCalendarTwo()
myCalendarTwo.book(10, 20)
myCalendarTwo.book(50, 60)
myCalendarTwo.book(10, 40)
myCalendarTwo.book(5, 15)
myCalendarTwo.book(5, 10)
myCalendarTwo.book(25, 55)

myCalendarTwo = MyCalendarTwo()
myCalendarTwo.book(26,35 )
myCalendarTwo.book(26, 32)
myCalendarTwo.book(25, 32)
myCalendarTwo.book(18,26 )
myCalendarTwo.book(40,45 )
myCalendarTwo.book(19,26 )
myCalendarTwo.book(48,50 )
myCalendarTwo.book(1,6 )
myCalendarTwo.book(46,50 )
myCalendarTwo.book(11,18 )