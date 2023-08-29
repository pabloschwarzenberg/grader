#Nota final
def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio_final, 1)

# Solicitar al usuario que ingrese las notas
pt = float(input("Ingrese la nota de las Tareas: "))
pi = float(input("Ingrese la nota de las Interrogaciones: "))
ne = float(input("Ingrese la nota del Examen: "))
pp = float(input("Ingrese la nota de la Presentación: "))

# Calcular el promedio final
promedio = calcular_promedio_final(pt, pi, ne, pp)

# Imprimir el resultado
print("El promedio final es:", promedio)
      