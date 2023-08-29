#Nota final
PT = float(input("Ingrese la nota de las tareas: "))
PI = float(input("Ingrese la nota de las interrogaciones: "))
NE = float(input("Ingrese la nota del exámen: "))
PP = float(input("Ingrese la nota de presentacion: "))

PR = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

print("El promedio final es", PR)
print("Fin")