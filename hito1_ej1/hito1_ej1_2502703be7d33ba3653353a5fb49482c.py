#Nota final
 
def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio, 1)

# Solicitar las notas al usuario
pt = float(input("Ingrese la nota de las tareas: "))
pi = float(input("Ingrese la nota de las interrogaciones: "))
ne = float(input("Ingrese la nota del examen: "))
pp = float(input("Ingrese la nota de la presentación: "))

# Calcular el promedio final
promedio_final = calcular_promedio_final(pt, pi, ne, pp)

# Imprimir el resultado
print("El promedio final es:", promedio_final)
 