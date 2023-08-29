#Nota final
PT = float(input("Nota de las Tareas:"))
PI = float(input("Nota de las Interrogaciones:"))
NE= float(input("Nota del Examen:"))
PP = float(input("Nota de la Presentacion:"))

PF= (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

print(round(PF,1))
