#Nota final
def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio_final, 1)

# Pedir al usuario que ingrese las notas
pt = float(input("Ingrese la nota de Tareas (PT): "))
pi = float(input("Ingrese la nota de Interrogaciones (PI): "))
ne = float(input("Ingrese la nota de Examen (NE): "))
pp = float(input("Ingrese la nota de Presentación (PP): "))

# Calcular el promedio final
promedio = calcular_promedio_final(pt, pi, ne, pp)

# Imprimir el promedio final redondeado a un decimal
print("El promedio final es:", promedio)