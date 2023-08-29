#Nota final
PT = float(input("ingrese nota de tareas: "))
PI = float(input("ingrese nota de interrogaciones: "))
NE = float(input("ingrese nota de Examen: "))
PP = float(input("ingrese nota de Presentacion: "))
notafinal = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("la nota final del curso es: ", round(notafinal, 1))      