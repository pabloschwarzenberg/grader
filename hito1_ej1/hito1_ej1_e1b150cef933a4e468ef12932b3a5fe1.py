#Nota final
PT = float(input("ingrese la nota de sus tareas: "))
PI = float(input("ingrese la nota de sus interrogaciones: "))
NE = float(input("ingrese la nota del examen: "))
PP = float(input("ingrese la nota de presentacion: "))
PROMEDIO_FINAL = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("promedio final es:", "{:.1f}".format(PROMEDIO_FINAL))
