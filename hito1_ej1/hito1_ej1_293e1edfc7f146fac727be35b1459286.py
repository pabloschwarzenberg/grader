#Nota final
PT = float(input("Ingrese nota en Tareas: "))
PI = float(input("Ingrese nota en Interrogaciones: "))
NE = float(input("Ingrese nota en Exámen: "))
PP = float(input("Ingrese nota en Presentación: "))

promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
print(round(promedio_final,1))