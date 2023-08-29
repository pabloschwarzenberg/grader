#Nota final
PT = float(input("Ingrese la nota de las Tareas: "))
PI = float(input("Ingrese la nota de las Interrogaciones: "))
NE = float(input("Ingrese la nota del Examen: "))
PP = float(input("Ingrese la nota de la Presentación: "))

promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
promedio = round(promedio, 1)

print(f"El promedio final es: {promedio}")
     