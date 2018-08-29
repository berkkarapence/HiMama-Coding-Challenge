import json
import sys


class Teacher(object):
    
    def __init__(self, first_name = "", last_name = "", teacher_id = None, clock_type = None, clock_time = None):
        self.first_name = first_name
        self.last_name = last_name
        self.clock_type = clock_type
        self.clock_time = clock_time
        
    def setFirstName(self, firstName):
        self.first_name = firstName
        
    def getFirstName(self):
        return self.first_name
        
    def setLastName(self, lastName):
        self.last_name = lastName
        
    def getLastName(self):
        return self.last_name
        
    def getName(self):
        name = self.first_name + " " + self.last_name
        return name
        
    def setTeacherId(self, id):
        self.teacher_id = id
        
    def getTeacherId(self):
        return self.teacher_id
        
    def setClockType(self, clockType):
        self.clock_type = clockType
        
    def getClockType(self):
        return self.clock_type
        
    def setClockTime(self, time):
        self.clock_time = time
        
    def getClockTime(self):
        return self.clock_time
        
    