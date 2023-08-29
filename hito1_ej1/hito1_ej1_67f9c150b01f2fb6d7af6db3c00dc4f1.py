#Nota final
PT = float(input("Ingrese el promedio de las tareas:"))
PI = float(input("Ingrese el promedio de las interrogaciones:"))
NE = float(input("Ingrese la nota del examen:"))
PP = float(input("Ingrese la nota de presentacion:"))
PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("El promedio final es:" ,round(PF,2))