#Nota final
PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de Examen: "))
PP = float(input("Ingrese la nota de Presentacion: "))
promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
promedio_final_redondeado = round(promedio_final, 1)
print("El promedio final es:", promedio_final_redondeado)     