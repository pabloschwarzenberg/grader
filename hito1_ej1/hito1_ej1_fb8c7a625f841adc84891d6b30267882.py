#Nota Final
PT = float(input("Ingrese la nota de la tareas: "))
PI = float(input("Ingrese la nota de las interrogaciones: "))
NE = float(input("Ingrese la nota de los examenes: "))
PP = float(input("Ingrese la nota de las presentaciones: "))

NotaFinal = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print("El promedio es :", "%.1f" % NotaFinal)