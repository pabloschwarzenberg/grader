#Nota final
# Por Matías Henríquez Gómez

import math

PT = float(input("Ingrese la nota de su tarea: "))
PI = float(input("Ingrese la nota de su interrogación: "))
NE = float(input("Ingrese la nota de su examen: "))
PP = float(input("Ingrese la nota de su presentación: "))

PT = PT * 0.3
PI = PI * 0.3
NE = NE * 0.3
PP = PP * 0.1

Promedio = (PT + PI + NE + PP)

Promedio = round(Promedio, 1)

print(Promedio)