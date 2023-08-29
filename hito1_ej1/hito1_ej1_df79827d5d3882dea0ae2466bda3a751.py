#Nota final
PT = float(input("Ingresa la nota de tu tarea: "))
PI = float(input("Ingresa la nota de la interrogación: "))
NE = float(input("Ingresa la nota del examen: "))
PP = float(input("Ingresa la nota de la presentación: "))

Promedio = ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))
print("El promedio es de: ",round(Promedio,1))