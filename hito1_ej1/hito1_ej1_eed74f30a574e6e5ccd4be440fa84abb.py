#Nota final
PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de iterrogaciones: "))
NE = float(input("Ingrese la nota de examen: "))
PP = float(input("Ingrese la nota de presentacion: "))
total = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print(round(total , 1))