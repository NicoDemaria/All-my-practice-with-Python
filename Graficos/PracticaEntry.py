from tkinter import *

Raiz=Tk()
Raiz.title("Pone tus datos de tarjeta y los tres ultimos numeros para salvar a ninja")
Raiz.config(bg="turquoise")
miFrame=Frame(Raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar() #ACA DEFINIMOS LA VARIABLE PERO NO ENTENDI MUY BIEN PARA QUE

cuadroNombre=Entry(miFrame, textvariable=minombre)  #CON ESTO CREAS EL CUADRO DE TEXTO DONDE PODES ECRIBIR
cuadroNombre.grid(row=0, column=1 )
cuadroNombre.config(bg="pink")
cuadroNombre.config(cursor="Hand1")
cuadroNombre.config(fg="white")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3, column=1 )
cuadroPass.config(bg="pink")
cuadroPass.config(cursor="pirate")
cuadroPass.config(show="X")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1 )
cuadroApellido.config(bg="pink")
cuadroApellido.config(cursor="pirate")

cuadroDirec=Entry(miFrame)
cuadroDirec.grid(row=2, column=1 )
cuadroDirec.config(bg="pink")   

TextoComentario=Text(miFrame, width=50, height=10) #ACA CREAMOS EL TEXTO DONDE SE PUEDE ESCRIBIR Y LE AGREGAMOS UNA ALTURA Y UN ANCHO
TextoComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=TextoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew") # CON EL COMANDO STICKY LO PEGAMOS A LA DERECHA

TextoComentario.config(yscrollcommand=scrollVert.set) #con esto ponemos mas o menos bien la barra de scroll

nombreLabel=Label(miFrame, text=("Nombre:"))
nombreLabel.grid(row=0, column=0)#, sticky="e,n,s,w" PARA ELEGIR LA POSICION   ) 
nombreLabel.config(bg="silver")

ApellidoLabel=Label(miFrame, text=("Apellido:"))
ApellidoLabel.grid(row=1, column=0) 
ApellidoLabel.config(bg="silver")

DirectLabel=Label(miFrame, text=("Direct:")) #CON ESTO Y EL GRID LO PONES DONDE QUERER Y LE AGREGAR UN PARAMETRO, NOMBRE EDAD ETC.
DirectLabel.grid(row=2, column=0,)
DirectLabel.config(bg="silver")

PassLabel=Label(miFrame, text=("Password:"))
PassLabel.grid(row=3, column=0) 
PassLabel.config(bg="silver")

ComentariosLabel=Label(miFrame, text=("Comentarios:"))
ComentariosLabel.grid(row=4, column=0) 
ComentariosLabel.config(bg="violet")

def codigoBoton():  #CON ESTA FUNCION VAMOS  A HACER QUE CUANDO TOQUEMOS EL BOTON SALGA NUESTRO NOMBRE

    minombre.set("Nicolas ") #ACA SETIAMOS EL NOMBRE PARA QUE LO IMPRIMA


botonEnvio=Button(Raiz, text="Enviar pa",command=codigoBoton)
botonEnvio.pack() #CON ESTO CREAMOS BOTONES 





Raiz.mainloop()