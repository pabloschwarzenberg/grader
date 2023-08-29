
def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio_final, 1)

tareas = float(input("Ingrese la nota de Tareas: "))
interrogaciones = float(input("Ingrese la nota de Interrogaciones: "))
examen = float(input("Ingrese la nota de Examen: "))
presentacion = float(input("Ingrese la nota de Presentación: "))

promedio = calcular_promedio_final(tareas, interrogaciones, examen, presentacion)

print("El promedio final es:", promedio)      