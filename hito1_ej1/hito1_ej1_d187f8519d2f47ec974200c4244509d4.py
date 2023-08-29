#Nota final
PT = float(input("Ingrese Promedio Tareas: "))
PI = float(input("Ingrese Promedio Interrogaciones: "))
NE = float(input("Ingrese Nota Examen: "))
PP = float(input("Ingrese Promedio Presentacion: "))
PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
xd = round(PF, 1)
print(xd)      