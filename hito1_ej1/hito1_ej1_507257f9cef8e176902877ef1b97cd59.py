#Nota final
PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de Examen: "))
PP = float(input("Ingrese la nota de Presentacion: "))

primedio = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

print("La nota final es:", round(primedio, 1))      