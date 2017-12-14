from tkinter import *

root = TK()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label="File", menu=submenu)

submenu.add_command(label="project", command=function1)
submenu.add_command(label="Save", command=function1)

submenu.add_seperator()
submenu.add_command(label="Exit", command=function1)

toolbar = Frame(root, bg="pink")
insertbutton = Button(toolbar, text = "Insert Files", command=function1)
insertbutton.pack(side=LEFT, padx=2, pady=3)

printbutton = Button(toolbar, text="print", command=function1)
printbutton.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=x)

root.mainloop()

# class MyButtons:
#     def _init_(self, rootone):
#         frame = Frame(rootone)
#         frame.pack()
#
#         self.printbutton = Button(frame, text="Click Here", command=self.printmessge)
#         self.printbutton.pack()
#
#         self.quitbutton = Button(frame, text="Exit", command=frame.quit)
#         self.quitbutton.pack(side=LEFT)
#
#     def printmessage(self):
#         print("Button Clicked")

# root = Tk()
# b = MyButtons(root)
#
# root.mainloop()