#Nota final
def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio_final, 1)

pt = float(input("Ingrese su nota de Tareas: "))
pi = float(input("Ingrese su nota de Interrogaciones: "))
ne = float(input("Ingrese su nota de Examen: "))
pp = float(input("Ingrese su nota de Presentación: "))

promedio = calcular_promedio_final(pt, pi, ne, pp)
print("El promedio final es: ", promedio)      