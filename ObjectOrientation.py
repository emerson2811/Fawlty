class Students:

    def init (self,name,contact):
        self.name = name
        self.contact = contact


    def getdata(self):
        print('Accepting data')
        self.name = input('Enter name')
        self.contact = input ('enter contact')

    def putdata(self):
        print('The name is:' + self.name, 'This is the contact:' + self.contact)

class ScienceStudent(Students):

    def init (self,age):
        self.age = age

    def science(selfs):
        print ("I am a science student")

Rob = ScienceStudent()
Rob.science()
Rob.getdata()
Rob.putdata()
#Functions inside of a class are called "methods"