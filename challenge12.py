# Coding challenge part 12
#
#
#
# Using the concept of object oriented programming and inheritance, create a super class named Computer, which has two sub classes named Desktop and Laptop.
#
#
# Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display the specifications of the computer.
#
#
# You can use any specifications which you want.
# The Desktop class and the Laptop class should have one specification which is exclusive to them for example laptop can have weight as a special specification.
#
#
# Make sure that the sub classes have their own methods to get and display their special specification.
#
# Create an object of laptop/ desktop and make sure to call all the methods from the computer class as well as the methods from the own class

class Computer:
    def __init__(self, ram, memory, processor):
        self.ram = ram
        self.memory = memory
        self.processor = processor

    def getspecs(self):
        print('Please enter the details')
        self.ram = input('Enter Ram Size')
        self.memory = input('Memory size')
        self.processor = input('Enter processor')

    def displayspecs(self):
        print('Here are the specs of the computer')
        print(' Ram size is: ' + self.ram + ' Memory size is: ' + self.memory + ' processor is: ' + self.processor)


class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor

    def get_case_details(self):
        self.casecolor = input('Enter case color')

    def put_case_details(self):
        print('case color is: ' + self.casecolor)


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def getweight(self):
        self.weight = input('Enter weight')

    def displayweight(self):
        print('weight is: ' + self.weight)


comp = Laptop('');

comp.getspecs()

comp.getweight()

comp.displayspecs()

comp.displayweight()