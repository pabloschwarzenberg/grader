#Nota final
PT = float(input("Ingrese la nota de las Tareas: "))
PI = float(input("Ingrese la nota de las Interrogaciones: "))
NE = float(input("Ingrese la nota del Examen: "))
PP = float(input("Ingrese la nota de la Presentación: "))

# Calcular el promedio final usando la fórmula dada
promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Redondear el resultado a un decimal
promedio_redondeado = round(promedio, 1)

# Imprimir el promedio final
print("El promedio final es:", promedio_redondeado)

      