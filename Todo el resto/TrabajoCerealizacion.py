import pickle

fichero=open("ListaNombres","rb")

lista=pickle.load(fichero) #Esto es para rescatar los archivos codificados en codigo binario

print(lista)















#lista_nombres=["Nicolas","Lucas","Pancha","Gaston"]

#fichero_binario=open("ListaNombres","wb")

#pickle.dump(lista_nombres, fichero_binario)   

#fichero_binario.close()


#del(fichero_binario)