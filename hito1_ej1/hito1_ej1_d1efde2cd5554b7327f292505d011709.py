#Nota final
import math
PT = float(input("ingrese su promedio de notas Tareas: "))
PI = float(input("ingrese su promedio de notas Ies: "))
NE = float(input("ingrese su nota de examen: "))
PP = float(input("ingrese su promedio de participación: "))
PF = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print(round(PF,2))
