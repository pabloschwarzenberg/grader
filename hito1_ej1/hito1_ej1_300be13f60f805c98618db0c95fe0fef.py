# Solicitar las notas al usuario
PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de Examen: "))
PP = float(input("Ingrese la nota de Presentacion: "))

# Calcular el promedio final
promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Imprimir el resultado redondeado a un decimal
print("El promedio final es:", round(promedio, 1))
