#Nota final
PT = float(input("Ingrese nota tareas: "))
PI = float(input("Ingrese nota interrogaciones: "))
NE = float(input("Ingrese nota examen: "))
PP = float(input("Ingrese nota presentación: "))

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
c = round(promedio, 1)
print(c)