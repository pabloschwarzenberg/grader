PT = float(input("ingrese la nota de las Tareas -> "))
Tareas = PT 
PI = float(input("ingrese la nota de las Interrogaciones -> "))
Interrogaciones = PI
NE = float(input("ingrese la nota del Examen -> "))
Examen = NE
PP = float(input("ingrese la nota de la Presentacion -> "))
Presentaciones = PP


NT = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(round(NT ,1))
