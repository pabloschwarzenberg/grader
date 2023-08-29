def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    promedio_redondeado = round(promedio, 1)
    return promedio_redondeado

# Solicitar al usuario que ingrese las cuatro notas
pt = float(input("Ingrese la nota de Tareas (PT): "))
pi = float(input("Ingrese la nota de Interrogaciones (PI): "))
ne = float(input("Ingrese la nota de Examen (NE): "))
pp = float(input("Ingrese la nota de Presentacion (PP): "))

# Calcular el promedio final llamando a la función
promedio_final = calcular_promedio_final(pt, pi, ne, pp)

# Imprimir el promedio final redondeado a un decimal
print("El promedio final es:", promedio_final)