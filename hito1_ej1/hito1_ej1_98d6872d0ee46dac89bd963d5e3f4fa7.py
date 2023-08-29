def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio_final, 1)

# Solicitamos al usuario ingresar las cuatro notas
pt = float(input("Ingrese la nota de PT (Tareas): "))
pi = float(input("Ingrese la nota de PI (Interrogaciones): "))
ne = float(input("Ingrese la nota de NE (Examen): "))
pp = float(input("Ingrese la nota de PP (Presentación): "))

# Calculamos el promedio final utilizando la fórmula
promedio_final = calcular_promedio_final(pt, pi, ne, pp)

# Imprimimos el resultado redondeado a un decimal
print("El promedio final es:", promedio_final)
