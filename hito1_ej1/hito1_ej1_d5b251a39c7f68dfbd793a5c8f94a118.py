#Nota final
def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    promedio_redondeado = round(promedio, 1)
    return promedio_redondeado

# Pedir al usuario que ingrese las cuatro notas
pt = float(input("Ingrese la nota de Tareas: "))
pi = float(input("Ingrese la nota de Interrogaciones: "))
ne = float(input("Ingrese la nota de Examen: "))
pp = float(input("Ingrese la nota de Presentación: "))

# Calcular el promedio final y redondearlo a un decimal
promedio_final = calcular_promedio_final(pt, pi, ne, pp)

# Imprimir el resultado
print("El promedio final es:", promedio_final)