   # Solicitar al usuario las cuatro notas
pt = float(input("Ingresa la nota de Tareas: "))
pi = float(input("Ingresa la nota de Interrogaciones: "))
ne = float(input("Ingresa la nota de Examen: "))
pp = float(input("Ingresa la nota de Presentación: "))

# Calcular el promedio final
promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp

# Redondear el promedio final a un decimal
promedio_final_redondeado = round(promedio_final, 1)

# Imprimir el resultado
print("El promedio final es:", promedio_final_redondeado)
