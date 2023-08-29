#Nota final
PT = float(input("Ingresa la nota de Tareas (PT): "))
PI = float(input("Ingresa la nota de Interrogaciones (PI): "))
NE = float(input("Ingresa la nota de Examen (NE): "))
PP = float(input("Ingresa la nota de Presentación (PP): "))
promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
promedio_redondeado = round(promedio, 1)
print("El promedio final es:", promedio_redondeado)      