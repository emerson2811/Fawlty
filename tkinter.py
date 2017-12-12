from tkinter import *

root = Tk()

#label1 = Label(root, text="Hello World")

#label1.pack()

newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)

button1 = Button(newframe, text = "Click Here", fg = "Red")

root.mainloop()
