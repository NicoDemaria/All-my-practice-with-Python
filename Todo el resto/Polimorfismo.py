class Coche():
	
	def dezplazamiento(self):
		print("Me dezplazo utilizando cuatro ruedas")

class Moto():
	
	def dezplazamiento(self):
		print("me dezplazo usando dos ruedas")


class Camion():
	
	 def dezplazamiento(self):
		 print("me dezplazo en 6 ruedas")

def dezplazamientoVehiculo(vehiculo):
	vehiculo.dezplazamiento()
MiVehiculo=Coche()

dezplazamientoVehiculo(MiVehiculo)
