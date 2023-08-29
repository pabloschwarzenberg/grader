#Nota final

PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de interrogaciones: "))
NE = float(input("Ingrese la nota de examen: "))
PP = float(input("Ingrese la nota de presentación: "))

promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

promedio_redondeado = round(promedio, 1)

print("\nEl promedio final es:", promedio_redondeado)
