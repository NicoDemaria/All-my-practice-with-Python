i=1

while i<=10:
	print("Ejecucion "+ str(i))
	i=i+1
print("Termino la ejecucion")

	




edad=int(input("introduce la edad por favor"))

while edad<5 or edad>100:	
	print("has una introducido una linea incorrecta")
	edad=int(input("introduce la edad por favor"))

print("Gracias por colaborar")

print("edad del aspirante " + str(edad))






import math

print("Programa de calculo de raiz cuadrado")
numero=int(input("Introduce un numero por favor:"))

intentos=0

while numero<0:
	print("No se puede halar la raiz de un numero negativo")

	if intentos==2:
		print("Has consumidos demasiados intentos el programa finalizo ")
		break;

	numero=int(input("Introduce un numero por favor:"))
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)	
	print("La raiz cuadra de " + str(numero) + "es" + str(solucion))	


