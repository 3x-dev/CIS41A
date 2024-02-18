'''
Aryan Singhal
CIS 41A   Winter 2024
Unit H, Exercise H
'''

# Part 1
class StateData:
    def __init__(self, name, abbreviation, region, population):
        self.name = name
        self.abbreviation = abbreviation
        self.region = region
        self.population = population
    
    def __str__(self):
        return self.name
    
    def displayState(self):
        print(f"{self.name} ({self.abbreviation}) is in the {self.region} region and has a population of {self.population}")

# Testing Part 1
s1 = StateData("California", "CA", "West", 39250000)
print(s1)  # Calls the __str__ method
s1.displayState()

# Part 2 
class StateData2:
    def __init__(self, name):
        self.name = name
    
    def setRegion(self, region):
        self.region = region
    
    def getRegion(self):
        return self.region

# Testing Part 2
s2 = StateData2("California")
s2.setRegion("West")
s2.pop = 39250000
print(s2.name)
print(s2.getRegion())
print(s2.region)
print(s2.pop)

# Part 3
class StateData3:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

# Testing Part 3
test = StateData3()
print(test.public)
print(test._protected)
try:
    print(test.__private)  # Raises an AttributeError
except AttributeError:
    print("Traceback error: 'StateData3' object has no attribute '__private'")


'''
Execution results:

California
California (CA) is in the West region and has a population of 39250000
California
West
West
39250000
Public
Protected
Traceback error: 'StateData3' object has no attribute '__private'
'''