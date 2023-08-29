#Nota final
def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio, 1)

# Solicitar al usuario ingresar las cuatro notas
pt = float(input("Ingresa la nota de Tareas (PT): "))
pi = float(input("Ingresa la nota de Interrogaciones (PI): "))
ne = float(input("Ingresa la nota de Examen (NE): "))
pp = float(input("Ingresa la nota de Presentación (PP): "))

# Calcular el promedio final
promedio_final = calcular_promedio_final(pt, pi, ne, pp)

# Imprimir el promedio final redondeado a un decimal
print("El promedio final es:", promedio_final)
