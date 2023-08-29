PT = float(input("ingrese la nota de la tarea: "))
PI = float(input("ingrese la nota por interrogacion: "))
NE = float(input("ingrese la nota del examen: "))
PP = float(input("ingrese la nota de presentacion: "))

final = round((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP), 1)

print("La nota final es: " +str(final))