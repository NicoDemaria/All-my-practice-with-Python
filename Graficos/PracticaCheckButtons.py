from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
ciudad=IntVar()
desierto=IntVar()

def opcionesViaje():
    
    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+="playa "
    if(ciudad.get()==1):
        opcionEscogida+="ciudad "
    if(desierto.get()==1):
        opcionEscogida+="desierto "
    textoFinal.config(text=opcionEscogida)    
    
    


Milabel=Label(root,text="Elegi tu destino")
Milabel.pack()

#foto=PhotoImage(file="Imagen de ejemplo bichin")
#Label(root, image=foto).pack

frame=Frame(root)
frame.pack()



Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Ciudad", variable=ciudad, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Desierto", variable=desierto, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()