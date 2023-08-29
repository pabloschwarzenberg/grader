#Nota final
# Pide al usuario que ingrese las cuatro notas
PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de Examen: "))
PP = float(input("Ingrese la nota de Presentacion: "))

# Calcula el promedio final utilizando la fórmula dada
promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Imprime el resultado redondeado a un decimal
print("El promedio final es:", round(promedio, 1))
