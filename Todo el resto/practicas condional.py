salariopresidente=int(input("Introduce salario presidente"))
print("Salarios presidente: " + str(salariopresidente))

salariodirector=int(input("Introduce salario director"))
print("Salarios presidente: " + str(salariopresidente))


salariojefearea=int(input("Introduce salario Jefe Area "))
print("Salarios presidente: " + str(salariopresidente))


salarioadministrativo=int(input("Introduce salario administrativo"))
print("Salarios presidente: " + str(salariopresidente))

if salarioadministrativo<salariojefearea<salariodirector<salariopresidente:
    print("Todo funciona piola")
else:
     print("algo nada para el orto en esta empresa de mierda")	

