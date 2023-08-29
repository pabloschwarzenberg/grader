#Nota final
def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio_final, 1)

pt = float(input("Ingresa la nota de las tareas (PT): "))
pi = float(input("Ingresa la nota de las interrogaciones (PI): "))
ne = float(input("Ingresa la nota del examen (NE): "))
pp = float(input("Ingresa la nota de la presentación (PP): "))

promedio = calcular_promedio_final(pt, pi, ne, pp)

print("El promedio final es:", promedio)