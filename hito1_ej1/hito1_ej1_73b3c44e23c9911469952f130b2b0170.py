#Nota final
PT = float(input("Introduzca nota Tareas: "))
PI = float(input("Introduzca nota Interrogaciones: "))
NE = float(input("Introduzca nota Examen: "))
PP = float(input("Introduzca nota Presentacion: "))

PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("El promedio final es: ", PF)