from tkinter import *

root=Tk()
root.config(bg="pink")
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
miImagen=PhotoImage(file="elduki.png")
miFrame.config(bg="yellow")
miFrame.config(cursor="pirate")
miFrame.config(bd="40")
miFrame.config(relief="groove")
Label(miFrame, image=miImagen).place(x=200, y=100)












root.mainloop()
