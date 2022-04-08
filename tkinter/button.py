from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "Look! I clicked a Button!")
    myLabel.pack()

# myButton = Button(root, text = "Click Me", padx = 50, pady = 50, state = DISABLED)
myButton = Button(root, text = "Click Me", command = myClick, fg = "blue", bg = "red") # when you call the function in your command do not use the parentheses; you can also use hex color codes
myButton.pack()

root.mainloop()