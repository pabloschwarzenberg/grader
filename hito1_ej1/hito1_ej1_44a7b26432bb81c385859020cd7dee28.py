def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio, 1)


# Solicitar al usuario las cuatro notas
pt = float(input("Ingrese la nota de PT (Tareas): "))
pi = float(input("Ingrese la nota de PI (Interrogaciones): "))
ne = float(input("Ingrese la nota de NE (Examen): "))
pp = float(input("Ingrese la nota de PP (Presentación): "))

# Calcular el promedio final
promedio_final = calcular_promedio_final(pt, pi, ne, pp)

# Imprimir el resultado
print("El promedio final es:", promedio_final)
