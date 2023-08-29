def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio_final, 1)

# Solicitar las notas al usuario
PT = float(input("Ingresa la nota de las Tareas: "))
PI = float(input("Ingresa la nota de las Interrogaciones: "))
NE = float(input("Ingresa la nota del Examen: "))
PP = float(input("Ingresa la nota de la Presentación: "))

# Calcular el promedio final
promedio = calcular_promedio_final(PT, PI, NE, PP)

# Imprimir el resultado
print("El promedio final es:", promedio)
