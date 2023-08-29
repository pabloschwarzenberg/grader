#Nota final
PT = float(input("Ingrese la nota obtenida en las tareas:"))
PI = float(input("Ingrese la nota obtenida en las interrogaciones:"))
NE = float(input("Ingrese la nota obtenida en el examen:"))
PP = float(input("Ingrese la nota obtenida en la presentación:"))
PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("El promedio final obtenido es:", round(PF,1))