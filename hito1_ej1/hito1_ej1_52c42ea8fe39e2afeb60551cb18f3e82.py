#Nota final
def calcular_promedio(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio, 1)

# Solicitar las cuatro notas al usuario
pt = float(input("Ingrese la nota de las Tareas (PT): "))
pi = float(input("Ingrese la nota de las Interrogaciones (PI): "))
ne = float(input("Ingrese la nota del Examen (NE): "))
pp = float(input("Ingrese la nota de la Presentación (PP): "))

# Calcular el promedio final
promedio_final = calcular_promedio(pt, pi, ne, pp)

# Imprimir el resultado redondeado a un decimal
print("El promedio final es:", promedio_final)
