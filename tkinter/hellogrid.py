# in the first tutorial we used pack to add the content to the window
# alternatively we can use the grid system

from tkinter import *

root = Tk() # this always has to go first in your gui code, it establishes the window

myLabel1 = Label(root, text = "Hello World!") # this creates our label widget
myLabel2 = Label (root, text = "this is using the grid formatting")

myLabel1.grid(row = 0, column = 0) # this adds the content to the window
myLabel2.grid(row = 1, column = 1)
# guis loop in order to track movement, so we need to create a loop so it can track your mouse across the screen, etc
root.mainloop()