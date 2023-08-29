#Nota final
from os import system
system ("cls")

PT = 0
PI = 0
NE = 0
PP = 0

PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de interrogaciones: "))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese la nota de la presentación: "))

promedio = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP, 1)
print(promedio)