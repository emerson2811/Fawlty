class Myclass:
    __hiddenvariable = 0
## double _ makes the variable "hidden" i.e. the varialbe cannot be called outside of the class

    def add(self, incremement):
        self.__hiddenvariable += incremement
        print(self.__hiddenvariable)

objectone = Myclass()
objectone.add(5)
print(objectone.__hiddenvariable)
