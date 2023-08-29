#Nota final
PT = float(input("ingrese la nota de la Tareas: "))
PI = float(input("ingrese la nota de la Interrogaciones: "))
NE = float(input("ingrese la nota del Examen: "))
PP = float(input("ingrese la nota de la Presentacion: "))

promedio = 0.3 *PT + 0.3*PI + 0.3*NE + 0.1*PP
promedio = round(promedio,1)

print(promedio)