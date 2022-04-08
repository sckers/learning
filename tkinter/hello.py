from tkinter import *

root = Tk() # this always has to go first in your gui code, it establishes the window

myLabel = Label(root, text = "Hello World!") # this creates our label widget

myLabel.pack() # this "packs" your label widget onto the screen

# guis loop in order to track movement, so we need to create a loop so it can track your mouse across the screen, etc
root.mainloop()
