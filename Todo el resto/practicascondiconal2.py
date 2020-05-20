print("Programa de becas breo")
distancia_escuela=int(input("Introduce la distancia en km"))
print(distancia_escuela)

numero_hermanos=int(input("Introduce numero de hermanos"))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto"))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:

     print("tienes derecho a beca")

else:
	print("No tienes derecho a beca por millonario xD")