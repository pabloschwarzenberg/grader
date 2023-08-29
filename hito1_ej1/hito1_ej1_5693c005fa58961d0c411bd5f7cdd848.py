#Nota final
def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio, 1)

# Pedimos al usuario que ingrese las cuatro notas
pt = float(input("Ingrese la nota de las Tareas: "))
pi = float(input("Ingrese la nota de las Interrogaciones: "))
ne = float(input("Ingrese la nota del Examen: "))
pp = float(input("Ingrese la nota de la Presentación: "))

# Calculamos el promedio final
promedio_final = calcular_promedio_final(pt, pi, ne, pp)

# Imprimimos el resultado redondeado a un decimal
print("El promedio final es:", promedio_final)
      