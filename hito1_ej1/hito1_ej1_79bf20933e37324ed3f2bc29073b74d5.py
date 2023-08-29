#Nota final
PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones:"))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese la nota de presentacion: "))
PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
PF = round(PF,1)
print("Su promedio final es:", PF)