#Creacion y apertura
from io import open

archivos_texto=open("archivo.txt","r")

archivos_texto.seek(len(archivos_texto.read())/2)

print(archivos_texto.read())





#print(archivos_texto.read())
#archivos_texto.seek(0)
#print(archivos_texto.read(11))










# archivos_texto.write("\n siempre es un buen momento para estudiar")



# a append
#w de write
# r de read



#lineas_texto=archivos_texto.readlines()

#archivos_texto.close()

#print(lineas_texto[1]) 









#texto=archivos_texto.read()

#archivos_texto.close()

#print(texto)









#frase="Estupendo dia para estudiar python \n el miercoles"
#Manipulacion
#archivos_texto.write(frase) 
#cierre el archivo desde memoria 
#archivos_texto.close()

#En el texto nos dice que dijimos clave 