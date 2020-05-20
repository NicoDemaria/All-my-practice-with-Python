class Coche():
	def __init__(self):


		self.largoChasis=250
		self.Anchochasis=120
		self.__ruedas=4
		self.enmarcha=False

	def arrancar(self,arrancamos):
		self.enmarcha=arrancamos

		if(self.enmarcha):
			chequeo=self.__chequeo_interno()

		if(self.enmarcha and chequeo):
		    return "El coche esta en marcha"
		
		elif(self.enmarcha and chequeo==False):
		 	return"algo anda mal en el chequeo no se pudo entrar"    

		else:
		 

		 	return "El coche esta parado"

	def estado(self):
		print("El coche tiene ", self.__ruedas, "ruedas")
		
	def __chequeo_interno(self):
		print("realizando chequeo interno")
		self.gasolina="ok"
		self.aceite="mal"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

			return True
		else:
			return False	




miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()


print(" ///A continuacion creamos el segundo objeto//////")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado() 