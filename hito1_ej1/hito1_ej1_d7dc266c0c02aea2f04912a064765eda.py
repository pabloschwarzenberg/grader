#Nota final
PT = float(input("Ingrese nota de Tareas: "))
PI = float(input("Ingrese nota de Interrogaciones: "))
NE = float(input("Ingrese nota de Examen: "))
PP = float(input("Ingrese nota de Presentación: "))

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
promedio = round(promedio, 1)
print("El promedio final es: ", promedio)