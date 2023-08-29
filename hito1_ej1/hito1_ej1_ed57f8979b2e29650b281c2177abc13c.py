def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio, 1)

# Obtener las notas del usuario
pt = float(input("Ingresa la nota de las Tareas: "))
pi = float(input("Ingresa la nota de las Interrogaciones: "))
ne = float(input("Ingresa la nota del Examen: "))
pp = float(input("Ingresa la nota de la Presentacion: "))

# Calcular el promedio final
promedio_final = calcular_promedio_final(pt, pi, ne, pp)

# Imprimir el resultado
print("El promedio final es:", promedio_final)
