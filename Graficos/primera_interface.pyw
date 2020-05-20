from tkinter import *
raiz=Tk()
raiz.title("Primera ventana de aplicacion ")
#raiz.resizable(0,0)
raiz.iconbitmap("el duki pa.ico")
#raiz.geometry("700x500")
raiz.config(bg="pink")
miFrame=Frame()
#miFrame.pack(side="left", anchor="s")
miFrame.pack()
miFrame.config(bg="green")
miFrame.config(width="650", height="350")
miFrame.config(bd=35)
miFrame.config(relief="groove")
miFrame.config(cursor="pirate")

raiz.mainloop()

