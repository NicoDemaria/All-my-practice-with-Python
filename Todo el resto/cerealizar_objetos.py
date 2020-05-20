import pickle

class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self): 

			self.enmarcha=True	
			
	def acelerar(self):
			self.acelera=True

	def frenar(self):
			self.frena=True

	def estado(self):
			print ("Marca: ", self.marca, "\nmodelo:  ", self.modelo, "\nEn marcha:  ", 
					self.enmarcha, "\nAcelerando:  ", self.acelera, "\nFrenado: "  , self.frena) 

coche1=Vehiculos("BMW","x6")
coche2=Vehiculos("Audi","x2")
coche3=Vehiculos("Ford","Ranger")

coches=[coche1,coche2,coche3]

fichero=open("LosCoches","wb")

pickle.dump(coches, fichero)

fichero.close()

del fichero

fichero_apertura=open("Loscoches","rb")

MisCoches=pickle.load(fichero_apertura)

fichero_apertura.close

for c in MisCoches:

    print(c.estado())       