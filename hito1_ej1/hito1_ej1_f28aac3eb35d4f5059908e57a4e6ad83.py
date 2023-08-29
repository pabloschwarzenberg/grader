def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio, 1)

# Solicitar al usuario ingresar las cuatro notas
pt = float(input("Ingrese la nota de Tareas (PT): "))
pi = float(input("Ingrese la nota de Interrogaciones (PI): "))
ne = float(input("Ingrese la nota de Examen (NE): "))
pp = float(input("Ingrese la nota de Presentación (PP): "))

# Calcular el promedio final
promedio_final = calcular_promedio_final(pt, pi, ne, pp)

# Imprimir el resultado
print("El promedio final es:", promedio_final)