from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Title", "This is awesome")

response = tkinter.messagebox.askquiest("Question1" , "Do you like coffee")

if repsonse == 'yes':
    print("Here is a coffee for you")