from tkinter import *

root = Tk()

# create an entry widget
#e = Entry(root, width = 50, bg = "blue", fg = "white", borderwidth = 5)
e = Entry(root, width = 50)
e.pack()
e.insert(0, "Enter your name")

def myClick():
    myLabel = Label(root, text = e.get())
    myLabel.pack()

# myButton = Button(root, text = "Click Me", padx = 50, pady = 50, state = DISABLED)
myButton = Button(root, text = "Click Me", command = myClick, fg = "blue", bg = "red") # when you call the function in your command do not use the parentheses; you can also use hex color codes
myButton.pack()

root.mainloop()