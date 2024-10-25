
# room.py
# Author sahwho
'''
    Represent a Room for Mod/Sim Fall 2024 Project 3 (MBHS)
    A Room has a roomNumber, an x and y position, and an urgency.
'''

import random

class room:
    def __init__(self, roomNumber, x, y, urgency):
        self.roomNumber = roomNumber
        self.x = x
        self.y = y
        self.urgency = urgency

    def getRoomNumber(self):
        return self.roomNumber

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getUrgency(self):
        return self.urgency

    # format the object for printing:
    def __str__(self):
        return 'room <' + str(self.roomNumber) + '> position: <' + str(self.x) + ',' + str(self.y) + '>, urgency: <' + str(self.urgency) + '>'

# sample usage
room101 = room(101, 4, 5, 17.9)
print(str(room101))
