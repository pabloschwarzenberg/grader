def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio_final, 1)

# Solicitar al usuario que ingrese las cuatro notas
pt = float(input("Ingresa la nota de las Tareas: "))
pi = float(input("Ingresa la nota de las Interrogaciones: "))
ne = float(input("Ingresa la nota del Examen: "))
pp = float(input("Ingresa la nota de la Presentación: "))

# Calcular el promedio final
promedio = calcular_promedio_final(pt, pi, ne, pp)

# Imprimir el resultado redondeado a un decimal
print("El promedio final es:", promedio)
      