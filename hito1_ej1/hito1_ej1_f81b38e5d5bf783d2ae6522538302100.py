#Nota final
NT = float(input("Ingrese nota de Tareas: "))
NI = float(input("Ingrese nota de Interrogaciones: "))
NE = float(input("Ingrese nota Examen: "))
NP = float(input("Ingrese nota Presentacion: "))

Promedio = ((0.3*NT)+(0.3*NI)+(0.3*NE)+(0.1*NP))
print("{0:.1f}".format(Promedio))