PT = float(input("Ingrese la nota de Tareas (PT): "))
PI = float(input("Ingrese la nota de Interrogaciones (PI): "))
NE = float(input("Ingrese la nota de Examen (NE): "))
PP = float(input("Ingrese la nota de Presentación (PP): "))

promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

print("El promedio final es:", round(promedio, 1))