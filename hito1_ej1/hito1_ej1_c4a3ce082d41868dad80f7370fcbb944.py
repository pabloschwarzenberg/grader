# Pedimos las cuatro notas al usuario
PT = float(input("Introduce la nota de Tareas: "))
PI = float(input("Introduce la nota de Interrogaciones: "))
NE = float(input("Introduce la nota de Examen: "))
PP = float(input("Introduce la nota de Presentación: "))

# Calculamos el promedio final utilizando la fórmula dada
promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

# Redondeamos el resultado a un decimal
promedio_redondeado = round(promedio, 1)

# Imprimimos el promedio redondeado
print("El promedio final es:", promedio_redondeado)