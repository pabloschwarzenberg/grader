#Nota final
def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio_final, 1)

pt = float(input("Ingrese la nota de las Tareas (PT): "))
pi = float(input("Ingrese la nota de las Interrogaciones (PI): "))
ne = float(input("Ingrese la nota del Examen (NE): "))
pp = float(input("Ingrese la nota de la Presentación (PP): "))

promedio = calcular_promedio_final(pt, pi, ne, pp)

print("El promedio final es:", promedio)