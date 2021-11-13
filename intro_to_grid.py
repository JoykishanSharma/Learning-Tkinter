from tkinter import *

root = Tk()

# creating a label widget
myLabel1 = Label(root, text="Hello, World!")
myLabel2 = Label(root, text="Some text")
myLabel3 = Label(root, text="Some text123")
myLabel4 = Label(root, text="Some text @123455")

# grid system
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=2, column=2)
myLabel4.grid(row=3, column=3)

root.mainloop()
