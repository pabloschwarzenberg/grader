#Nota final
import math
PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de interrogaciones: "))
NE = float(input("Ingrese la nota de examen: "))
PP = float(input("Ingrese la nota de presentacion: "))

nota_final = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
redondeado = round(nota_final, 1)
print(redondeado)