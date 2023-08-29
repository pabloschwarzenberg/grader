#Nota final

#ENTRADA

PT= float(input("ingrese nota Tareas: "))
PI= float(input("ingrese nota Interrogación: "))
NE= float(input("ingrese nota Examen: "))
PP= float(input("ingrese nota Presentación: "))

#DESARROLLO

PF= (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
PF= round(PF,1)

#SALIDA

print("El promedio final es:" , PF)
