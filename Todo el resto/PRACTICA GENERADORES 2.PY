def devuelveCiudades(*ciudades):
 	for elemento in ciudades:
 		#for subelemnto in elemento:
 		    yield from elemento

ciudadesDevueltas=devuelveCiudades("Madrid","Cordoba","Barcelona","BSAS")

print(next(ciudadesDevueltas))	

print(next(ciudadesDevueltas))					