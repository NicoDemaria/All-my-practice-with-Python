from tkinter import *

Raiz=Tk()
Raiz.config(bg="grey")
Raiz.title("Calculadora basica")


Miframe=Frame(Raiz)

Miframe.pack()

operacion=""

resultado=0

#Pantalla

numeroPantalla=StringVar()


Pantalla=Entry(Miframe, textvariable=numeroPantalla)
Pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
Pantalla.config(bg="black", fg="green", justify="r")

#----------------Funcionamiento-------------

def numeroPulsado(num):

    global operacion

    if operacion!="":

        numeroPantalla.set(num)

        operacion=""
    else: 


        numeroPantalla.set(numeroPantalla.get() + num)


#VER DE NUEVO EL VIDEO 49 PORQUE QUEDARON DUDAS F

#------------funcion suma------------

def suma(num):

    global operacion

    global resultado

    resultado+=int(num)

    operacion="suma"  

    numeroPantalla.set(resultado)    

#------Funcion el_resultado------

def el_resultado():
    global resultado

    numeroPantalla.set(resultado+int(numeroPantalla.get()))    
    resultado=0

#----------------Fila 1-------------

boton7=Button(Miframe, text="7", width=3, bg="turquoise", command=lambda:numeroPulsado("7") )
boton7.grid(row=2, column=1,pady=5)
boton8=Button(Miframe, text="8", width=3, bg="pink", command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2,pady=5)
boton9=Button(Miframe, text="9", width=3, bg="turquoise", command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3,pady=5)
botonDiv=Button(Miframe, text="/", width=3, bg="violet")
botonDiv.grid(row=2, column=4,pady=5)

#----------------Fila 2-------------

boton4=Button(Miframe, text="4", width=3, bg="pink", command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1,pady=5)
boton5=Button(Miframe, text="5", width=3, bg="turquoise", command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2,pady=5)
boton6=Button(Miframe, text="6", width=3, bg="pink",command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3,pady=5)
botonMult=Button(Miframe, text="X", width=3,bg="pink")
botonMult.grid(row=3, column=4,pady=5)

#----------------Fila 3-------------

boton1=Button(Miframe, text="1", width=3,bg="turquoise",command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1,pady=5)
boton2=Button(Miframe, text="2", width=3, bg="pink",command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2,pady=5)
boton3=Button(Miframe, text="3", width=3,bg="turquoise",command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3,pady=5)
botonRestar=Button(Miframe, text="-", width=3,bg="violet")
botonRestar.grid(row=4, column=4,pady=5)

#----------------Fila 4-------------

boton0=Button(Miframe, text="0", width=3, bg="violet",command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1,pady=5)
botonComa=Button(Miframe, text=",", width=3, bg="pink",command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=2, pady=5)
botonIgual=Button(Miframe, text="=", width=3, bg="violet", command=lambda:el_resultado())
botonIgual.grid(row=5, column=3, pady=5)
botonSuma=Button(Miframe, text="+", width=3, bg="pink", command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4,pady=5)

























Raiz.mainloop()




