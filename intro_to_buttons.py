from tkinter import *

root = Tk()


# function
def my_click():
    my_label = Label(root, text="Some text is appearing!")
    my_label.pack()


# creating a button
my_button = Button(root, text="Click Me!", padx=20, pady=50, command=my_click, fg="white",
                   bg="black")

# adding to the screen
my_button.pack()

root.mainloop()
