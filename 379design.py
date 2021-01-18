from collections import OrderedDict

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.maxNumbers = maxNumbers
        self.l = [True] * maxNumbers

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        i = 0
        while i < self.maxNumbers:
            if self.l[i]:
                self.l[i] = False
                return i
            i += 1
        return -1



    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return self.l[number]

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.l[number] = True


directory = PhoneDirectory(3)
print(directory.get())

print(directory.get())

print(directory.check(2))

print(directory.get())

print(directory.check(2))

print(directory.release(2))

print(directory.check(2))