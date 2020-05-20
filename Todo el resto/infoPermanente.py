import pickle

class Persona:
    def __init__(self, nombre, genero, edad ):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se creo una persona nueva con el nombre de:", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)



class ListaPersonas:

    personas=[]
    
    def __init__(self):

        listaDePersonas=open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)
        try:    
                self.personas=pickle.load(listaDePersonas)  
                print("Se cargaron {} personas del fichero externo".format(len(self.personas)))  
        except:   
                print("El fichero esta vacio")  

        finally:
                listaDePersonas.close() 
                del(listaDePersonas)




    def agregarPersonas(self, p):
        self.personas.append(p)
        self.GuardasPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    def GuardasPersonasEnFicheroExterno(self):
        ListaPersonas=open("ficheroExterno", "wb") 
        pickle.dump(self.personas, ListaPersonas)
        ListaPersonas.close()
        del(ListaPersonas)     
    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero es la siguiente:")
        for p in self.personas: 
            print (p)      

miLista=ListaPersonas()
persona=Persona("Antonio", "masculino", "49")
miLista.agregarPersonas(persona)


#p=Persona("Sandra", "Mujer", 95) 
#miLista.agregarPersonas(p)
#p=Persona("toto", "masculino", 15) 
#miLista.agregarPersonas(p)
#p=Persona("pancho", "femenino", 35) 
#miLista.agregarPersonas(p)

#miLista.mostrarPersonas()