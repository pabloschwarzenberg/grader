PT = float(input("Ingrese la nota de Tareas (0-100): "))
PI = float(input("Ingrese la nota de Interrogaciones (0-100): "))
NE = float(input("Ingrese la nota de Examen (0-100): "))
PP = float(input("Ingrese la nota de Presentación (0-100): "))

promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
promedio_redondeado = round(promedio, 1)
print("El promedio final es:", promedio_redondeado)
