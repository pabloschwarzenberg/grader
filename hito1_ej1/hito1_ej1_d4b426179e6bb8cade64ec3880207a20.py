# Solicitar las cuatro notas al usuario
PT = float(input("Ingrese la nota de las Tareas (0-100): "))
PI = float(input("Ingrese la nota de las Interrogaciones (0-100): "))
NE = float(input("Ingrese la nota del Examen (0-100): "))
PP = float(input("Ingrese la nota de la Presentación (0-100): "))

# Calcular el promedio final
promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Imprimir el promedio final redondeado a un decimal
print("El promedio final es:", round(promedio_final, 1))
      