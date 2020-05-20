from tkinter import *

root=Tk()

BarraMenu=Menu(root)
root.config(menu=BarraMenu, width=300, height=300)

archivoMenu=Menu(BarraMenu, tearoff=0)

archivoEdicion=Menu(BarraMenu, tearoff=0)
archivoEdicion.add_command(label="copiar")
archivoEdicion.add_command(label="pegar")
archivoEdicion.add_command(label="cortar")


archivoHerramientas=Menu(BarraMenu)


archivoAyuda=Menu(BarraMenu)
archivoMenu.add_command(label="nuevo")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="guardar")
archivoMenu.add_command(label="salir")




BarraMenu.add_cascade(label="archivo", menu=archivoMenu)


BarraMenu.add_cascade(label="edicion", menu=archivoEdicion)

BarraMenu.add_cascade(label="herramienta", menu=archivoHerramientas)



BarraMenu.add_cascade(label="ayuda", menu=archivoAyuda)





root.mainloop()