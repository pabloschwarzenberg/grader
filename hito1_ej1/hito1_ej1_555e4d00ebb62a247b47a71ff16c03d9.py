# Solicitar al usuario las cuatro notas
pt = float(input("Ingrese la nota de Tareas: "))
pi = float(input("Ingrese la nota de Interrogaciones: "))
ne = float(input("Ingrese la nota de Examen: "))
pp = float(input("Ingrese la nota de Presentación: "))

# Calcular el promedio final
promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp

# Redondear el resultado a un decimal
promedio_redondeado = round(promedio, 1)

# Imprimir el resultado
print("El promedio final es:", promedio_redondeado)
      