from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sarah's Cool App")
root.iconbitmap('C:/Users/scker/Downloads/artboard-12_89035.ico')

my_img = ImageTk.PhotoImage(Image.open('tree_image3.png'))


my_label = Label(image = my_img)
my_label.pack()









button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack()










root.mainloop()