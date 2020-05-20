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

class Furgoneta(Vehiculos):

	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgo esta cargada"
		else: 
			return	"La furgo no esta cargada"
			


class Moto(Vehiculos): 
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito "

	def estado(self):
			print ("Marca: ", self.marca, "\nmodelo:  ", self.modelo, "\nEn marcha:  ", 
					self.enmarcha, "\nAcelerando:  ", self.acelera, "\nFrenado: "  , self.frena, "\n", self.hcaballito	)	
		
class VElectricos(Vehiculos):
	def __init__(self, marca, modelo):

		super().__init__(marca, modelo)
		self.autonomia=100
	def CargarEnergia(self):
		self.cargando=True	


miMoto=Moto("Honda", "CBR")

miMoto.caballito()

miMoto. estado()	

MiFurgoneta=Furgoneta("Renault", "Kangoo")

MiFurgoneta.arrancar()

MiFurgoneta.estado()

print(MiFurgoneta.carga(True))

class BicicletaElectrica(Vehiculos, VElectricos):
	
	pass

MiBici=BicicletaElectrica("Venzo", "laputamadre")		










			
	